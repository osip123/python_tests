import turtle as t


def main():
    t.setup(500, 500)
    t.bgcolor('green')
    t.color('red')
    t.speed(100)
    t.left(120)
    t.forward(100)

    for i in range(19):
        t.left(i)

if __name__ == '__main__':
    while True:
        main()