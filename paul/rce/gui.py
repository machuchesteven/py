import tkinter as tk

from window import window
from christmas1 import make_session
from thread import make_thread

make_thread(make_session)
window().mainloop()
