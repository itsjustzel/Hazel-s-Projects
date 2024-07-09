import imageio.v3 as iio

def main():
    filenames = ['team-pic1.png', 'team-pic2.png']
    images = []

    for filename in filenames:
        images.append(iio.imread(filename))
        
    iio.imwrite('team.gif', images, duration = 500, loop = 0)

if __name__ == "__main__":
    main()