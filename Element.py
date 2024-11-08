import Image


class Element():
    def __init__(self,type ):
        self.chosen = 0

        self.images_list = []

        for i in range(1,4):
            path = f"images/{type}{i}.png"

        loaded_images=Image(path)
        self.images_list.append(loaded_images)

    def chosenext(self):
        self.chosen +=1
        if self.chosen>2:
            self.chosen=0

    def chosenimage(self):
        return self.images_list[self.chosen].Image


