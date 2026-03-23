
def numpy():
    import numpy as np

    print(np.array([1, 2, 3]))
    print(np.zeros((3, 4)))
    print(np.ones((3, 4)))
    print(np.arange(1, 9))
    print(np.linspace(1, 9, 3))

    A = np.array([[1, 1], [0, 1]])
    B = np.array([[2, 0], [3, 4]])
    print(A + 2)
    print(B ** 2)
    print(A + B)

def tinker():
    import tkinter as tk

    root = tk.Tk()
    tk.Label(root, text="Hello").grid(row=0, column=0)
    tk.Label(root, text="World").grid(row=1, column=2)

    root.mainloop()


def matplotlib():
    import matplotlib.pyplot as plt
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    jahre = [2013, 2017, 2021, 2025]
    stimmen_spd = [26, 21, 26, 16]
    ax1.plot(jahre, stimmen_spd)
    ax1.set_xticks([2013, 2017, 2021, 2025])
    ax1.set_xlabel('Wahljahr')
    ax1.set_ylabel('Stimmenanteil (%)')
    ax1.set_title('SPD Wahlergebnisse')
    parteien = ['CDU/CSU', 'SPD', 'AfD']
    ergebnisse = [29, 16, 21]
    ax2.bar(parteien, ergebnisse)
    ax2.set_xlabel('Partei')
    ax2.set_ylabel('Stimmenanteil (%)')
    ax2.set_title('Bundestagswahl 2025')
    plt.show()

def f(a, b = 42):
    print(d)
    print(b)


if __name__ == '__main__':
    d = 17
    f(1, d)
