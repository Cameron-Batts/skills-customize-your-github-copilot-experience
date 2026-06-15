from helpers import greet_user, calculate_area, format_result


def main():
    name = input("Enter your name: ")
    print(greet_user(name))

    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    area = calculate_area(width, height)

    print(format_result(name, area))


if __name__ == "__main__":
    main()
