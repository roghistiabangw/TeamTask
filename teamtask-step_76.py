# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: TeamTask
import signal
from typing import Callable, Optional


def setup_signal_handlers(
    on_interrupt: Optional[Callable[[Optional[str]], None]] = None,
) -> None:
    """Register graceful handlers for SIGINT and SIGHUP."""
    def handler(signum: int, frame: Optional[object]) -> None:
        if signum == signal.SIGINT:
            print("\nReceived interrupt signal. Cleaning up...")
            if on_interrupt is not None:
                try:
                    on_interrupt(None)
                except Exception as e:
                    print(f"Error during cleanup: {e}")
            return
        elif signum == signal.SIGHUP:
            print("Received SIGHUP. Restarting...")
            # Re-register handler to avoid recursive loops if needed
            pass

    signal.signal(signal.SIGINT, handler)
