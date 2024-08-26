try:
    import js
    import pyodide
    import pyodide_js
    import pyodide_kernel
except ImportError:
    # no-op outside of a JupyterLite notebook
    pass
else:
    js.__ipyloglite_pyodide = pyodide_js

    pyodide.code.run_js(r"""
// Save the original console.log and console.error methods
if (this.__console_log === undefined) {
    this.__console_log = console.log;
}
if (this.__console_error === undefined) {
    this.__console_error = console.error;
}

function jupyterlite_console_capture(stream, fallback, ...args) {
    // Only capture simple messages for now
    for (const arg of args) {
        if (typeof(arg) !== "string") {
            return fallback(...args);
        }
    }

    const message = args.join(" ") + "\n";

    // Reduce noise by ignoring
    // "PACKAGE already loaded from CHANNEL channel"
    // messages
    if (
        message.includes(" already loaded from ") &&
        message.endsWith(" channel\n")
    ) {
        return fallback(...args);
    }

    // Reduce noise by ignoring "No new packages to load" messages
    if (message === "No new packages to load\n") {
        return fallback(...args);
    }

    // Ensure that the JupyterLite stream callback is initialised
    if (this.__ipyloglite_jupyterlite_stream_callback === undefined) {
        this.__ipyloglite_jupyterlite_stream_callback =
            this.__ipyloglite_pyodide.runPython(
                "import pyodide_kernel;" +
                "pyodide_kernel.sys.stdout.publish_stream_callback"
            );
        delete this.__ipyloglite_pyodide;
    }

    // Forward the message to the Jupyter cell output
    this.__ipyloglite_jupyterlite_stream_callback(
        stream, "[pyodide]: " + message
    );

    return fallback(...args);
}

// Remap the console.log and console.error methods
console.log = (...args) => jupyterlite_console_capture(
    "stdout", __console_log, ...args,
);
console.error = (...args) => jupyterlite_console_capture(
    "stderr", __console_error, ...args,
);
    """)
