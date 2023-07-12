try:
    import pyodide
except ImportError:
    # no-op outside of a JupyterLite notebook
    pass
else:
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

    // Forward the message to the Jupyter cell output
    postMessage({
        bundle: {
            name: stream,
            text: "[pyodide]: " + message,
        },
        type: "stream",
    });

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
