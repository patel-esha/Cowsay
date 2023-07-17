from dragon import Dragon


class IceDragon(Dragon):

    def __init__(self, name, image):
        super().__init__(name, image)

    def can_breathe_fire():
        print('This dragon cannot breathe fire.')
        return False
