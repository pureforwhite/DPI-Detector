import ctypes
import sys

def get_mouse_sensitivity():
    SPI_GETMOUSESPEED = 0x0070
    mouse_speed = ctypes.c_int()
    ctypes.windll.user32.SystemParametersInfoA(SPI_GETMOUSESPEED, 0, ctypes.byref(mouse_speed), 0)
    return mouse_speed.value

def get_dpi():
    try:
        from ctypes import windll
        user32 = windll.user32
        user32.SetProcessDPIAware()
        [width, height] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
        print(f"Screen resolution: {width}x{height}")
    except ImportError:
        print("Error: could not load ctypes module")
        sys.exit(1)

    hdc = windll.user32.GetDC(0)
    dpi = windll.gdi32.GetDeviceCaps(hdc, 88)  # LOGPIXELSX
    windll.user32.ReleaseDC(0, hdc)
    return dpi

def main():
    mouse_sensitivity = get_mouse_sensitivity()
    screen_dpi = get_dpi()
    print(f"Mouse sensitivity (Windows setting): {mouse_sensitivity}")
    print(f"Screen DPI: {screen_dpi}")

if __name__ == "__main__":
    main()
