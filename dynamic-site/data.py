"""
# ELIMARIE MORALES SANTIAGO
# FULL SAIL UNIVERSITY
# Design Patterns for Web Programming - Online
# Dynamic Site
"""


class GemstoneInfo(object):
    def __init__(self):
        # Data attribute for object gemstone
        opal = Gemstone()
        opal.name = 'The Opal'
        opal.bio = 'The Opal is a type of quartz. Is a gem-quality <br> form of hydrated amorphous silicon dioxide.'
        opal.origin = 'The origin of name develops from Sanskrit  which is a classical Indian language meaning upala equal to precious stone. It is gemologically classed as a mineraloid rather than a mineral, owing to its amorphous form.'
        opal.story = ' The ancient Greeks thought opal to be the tears of Zeus and prized it as highly as diamonds. They believed opal gave the gift of foresight and prophecy, which would ensure the owner\'s success in war, business and life.'
        opal.locations = 'Opals are found in the regions of Mexico, Brazil, USA, Japan, Honduras, Kenya, Czechoslovakia, Peru, Canada but by far Australia is the main source of opals, almost ninety-five per cent of all fine opals come from the dry and remote outback deserts.'
        opal.colors = 'Color: White, luminous and iridescent with inclusions of many colours. Opals show a shifting of spectral colors.'
        opal.img = 'img/opal.png'

        # Data attribute for object gemstone
        amethyst = Gemstone()
        amethyst.name = 'The Amethyst'
        amethyst.bio = 'Is the most precious gemstone within the quartz group.'
        amethyst.origin = 'The origin of name from the Greek amethystos, which means not drunken. This precious gemstone was considered to be a strong antidote against drunkenness.'
        amethyst.story = 'A Greek legend tells the story of a maiden Amethystos who was pursued by a drunken god called Dionysus. She prayed to the goddess Artemis for help and ask her to let her remain a virgin. The goddess kindly granted her prayer, transforming her into a pure white stone. Dionysus filled with remorse cried tears of wine over the stone, turning it purple.'
        amethyst.locations = 'Amethyst are mined in Brazil, Uruguay, Bolivia, Argentina, Zambia, Namibia and other African countries.'
        amethyst.colors = 'Colour: Amethyst ranges in color, from pale lilac to deep reddish-purple.'
        amethyst.img = 'img/amethyst.png'

        # Data attribute for object gemstone
        diamond = Gemstone()
        diamond.name = 'The Diamond'
        diamond.bio = 'The Diamond is a crystalline quality gemstone <br> formed of carbon and it is the hardest known natural substance on earth.'
        diamond.origin = 'The origin of name develops from Greek, was taken from word, \'adamas\', meaning invincible.'
        diamond.story = 'The magnificent physical qualities of diamonds are credited to the strong chemical bonds formed between atoms. Each individual carbon atom is connected to four other carbon atoms, all of which are very closely packed. This formation produce a strong, and completely symmetrical three-dimensional cubic structure. Allowing diamonds to refract light in all directions at the same velocity.'
        diamond.locations = 'Diamonds are found in the regions of Africa, Asia, Russia, India, North America, Canada, USA, Oceania, and Australia.'
        diamond.colors = 'Color: Transparent, Blue, pink, red, green, orange and black. Red diamonds are actually one of the rarest gemstones in the world. The color of red diamonds is the unique result of minute defects formed in the symmetrical three-dimensional arrangement of atoms inside a crystal.'
        diamond.img = 'img/diamond.png'

        # Data attribute for object gemstone
        topaz = Gemstone
        topaz.name = 'The Topaz'
        topaz.bio = 'The Topaz is an aluminium silicate that contains fluorine and hydroxyl. <br> In its pure form it is colorless. Impurities cause different colours within the Topaz.'
        topaz.origin = 'The origin of name develops from Greek Topazion, a Red Sea Island often covered in mist. The name of the island means to seek in Greek.'
        topaz.story = 'Ancient Egyptians believed that yellow topaz received its golden hue from the Sun God, Ra.'
        topaz.locations = 'Deposits of topaz are found in the regions of Russia, Siberia, Brazil, Sri Lanka, Africa and China, Japan, Pakistan, Myanmar, Nigeria, Australia, Mexico, and in the United States.'
        topaz.colors = 'Yellow, blue, pink, peach, gold, green, red, and brown. It is often heated to change or enhance it\'s colour.'
        topaz.img = 'img/topaz.png'

        # Data attribute for object gemstone
        tourmaline = Gemstone()
        tourmaline.name = 'The Tourmaline'
        tourmaline.bio = 'Tourmaline is one of the most versatile of gemstone of the silicate group, and <br> there are 10 different varieties created by the dozen or more elements they contain.'
        tourmaline.origin = 'The origin of name develops from Sinhalese turamali which means stone with various colors in reference to its extreme versatility. '
        tourmaline.story = 'Tourmaline is found in every color. It can show every tone from pastel to dark, and can display various colors in the same stone. Others display a mobile, wavering striped reflection.'
        tourmaline.locations = 'Tourmaline is found in Africa, Brazil, Madagascar, Mexico, Myanmar, Namibia, Sri Lanka and USA.'
        tourmaline.colors = 'Variety green, red to pink, light to dark blue, colourless, purple , neon blue, brown, black, red to green and green to red. Tourmaline may be heated to enhance its color.'
        tourmaline.img = 'img/tourmaline.png'

        # ad object to objects array
        self.list = [opal, amethyst, diamond, topaz, tourmaline]


# class created to use with the other py files
class Gemstone(object):
    # init variable
    def __init__(self):
        # Declaration for same attributes as data objects
        self.name = ''
        self.bio = ''
        self.origin = ''
        self.story = ''
        self.locations = ''
        self.colors = ''
        self.img = ''
