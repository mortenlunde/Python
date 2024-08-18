def calculate_fold(folds):
    width = 297
    length = 210
    thickness = 0.1

    for i in range (folds):
        if width > length:
            width /= 2
        else:
            length /= 2

        thickness *= 2

    return width,length,thickness

def main():
    folds = int(input("Enter the number of times you want to fold the paper (a4): "))
    width,length,thickness = calculate_fold(folds)
    width_cm = width / 10
    length_cm = length / 10
    thickness_cm = thickness / 10
    width_m = width_cm / 1000
    length_m = length_cm / 1000
    thickness_m = thickness_cm / 1000
    print(f'The paper is now {width}mm wide, {length}mm high, and {thickness}mm thick.')
    print(f'The paper is now {width_cm}cm wide, {length_cm}cm high, and {thickness_cm}cm thick.')
    print(f'The paper is now {width_m}m wide, {length_m}m high, and {round(thickness_m)}m thick.')

    if thickness_m > 828:
        print("This is thicker than the hight of Burj Khalifa (828 meters)")
    if thickness_m > 8848.86:
        print("This is thicker than the hight of Mount Everest (8848.86 meters)")
    if thickness_m > 38400000:
        print("This is thicker than the distance to the moon (384.000 km)")

if __name__ == '__main__':
    main()