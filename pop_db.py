#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Breed, Base

engine = create_engine('sqlite:///catalog_proj.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Categories

# Sporting Group
cat1 = Category(name="Sporting")
session.add(cat1)
session.commit()

breed1 = Breed(
    name="Brittany",
    description="Sportsmen on both sides of the Atlantic cherish the "
                "agile, energetic Brittany as a stylish and versatile "
                "gundog. Bright and eager at home, and tireless afield, "
                "Brittanys require a lot of exercises, preferably with "
                "their favorite humans.",
    category=cat1, rank=26,
    photo_attribution="Pharaoh Hound [CC BY-SA 3.0 ("
                      "https://creativecommons.org/licenses/by-sa/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/a/af/"
          "Brittany_Spaniel_standing.jpg")
session.add(breed1)
session.commit()

breed2 = Breed(
    name="Chesapeake Bay Retriever",
    description="The Chesapeake Bay Retriever, peerless duck dog of the "
                "Mid-Atlantic, is an American original who embodies the "
                "classic traits of a good retriever: loyal, upbeat, "
                "affectionate, and tireless. The Chessie is famous for "
                "his waterproof coat.",
    category=cat1, rank=43,
    photo_attribution="Keith Rousseau at en.wikipedia [CC BY-SA 3.0 ("
                      "http://creativecommons.org/licenses/by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/7/7c/"
          "Chesapeake_Bay_Retriever1.jpg")
session.add(breed2)
session.commit()

breed3 = Breed(
    name="Labrador Retriever",
    description="The sweet-faced, lovable Labrador Retriever is America's "
                "most popular dog breed. Labs are friendly, outgoing, and "
                "high-spirited companions who have more than enough "
                "affection to go around for a family looking for a "
                "medium-to-large dog.",
    category=cat1, rank=1,
    photo_attribution="Annosaris [CC BY 3.0 ("
                      "https://creativecommons.org/licenses/by/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/4/48/"
          "Dafje_the_Labrador_Retriever.jpg")
session.add(breed3)
session.commit()

breed4 = Breed(
    name="Golden Retriever",
    description="The Golden Retriever, an exuberant Scottish gundog of "
                "great beauty, stands among America's most popular dog "
                "breeds. They are serious workers at hunting and field "
                "work, as guides for the blind, and in search-and-rescue, "
                "enjoy obedience and other competitive events, and have an "
                "endearing love of life when not at work.",
    category=cat1, rank=3,
    photo_attribution="Dirk Vorderstra&szlig;e [CC BY 3.0 ("
                      "https://creativecommons.org/licenses/by/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/1/1d/"
          "Golden_retriever_stehfoto.jpg")
session.add(breed4)
session.commit()

breed5 = Breed(
    name="German Shorthaired Pointer",
    description="The versatile, medium-sized German Shorthaired Pointer is "
                "an enthusiastic gundog of all trades who thrives on "
                "vigorous exercise, positive training, and a lot of love. "
                "GSP people call their aristocratic companions the "
                "\"perfect pointer.\"",
    category=cat1, rank=10,
    photo_attribution="Bonnie van den Born, http://www.bonfoto.nl "
                      "[CC BY-SA 3.0 (http://creativecommons.org/"
                      "licenses/by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/3/38/"
          "Duitse_staande_korthaar_10-10-2.jpg")
session.add(breed5)
session.commit()

breed6 = Breed(
    name="English Springer Spaniel",
    description="The English Springer Spaniel is a sweet-faced, lovable "
                "bird dog of great energy, stamina, and brains. Sport "
                "hunters cherish the duality of working Springers: "
                "handsome, mannerly pets during the week, and trusty "
                "hunting buddies on weekends.",
    category=cat1, rank=27,
    photo_attribution="photo taken by Heinz H&ouml;fling [User:Hhoefling] "
                      "[CC BY-SA 3.0 (http://creativecommons.org/licenses/"
                      "by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/5/5c/"
          "English-Springer-Spaniel-Coffee2.jpg")
session.add(breed6)
session.commit()

breed7 = Breed(
    name="Cocker Spaniel",
    description="The merry and frolicsome Cocker Spaniel, with his big, "
                "dreamy eyes and impish personality, is one of the world's "
                "best-loved breeds. They were developed as hunting dogs, "
                "but Cockers gained their wide popularity as all-around "
                "companions.",
    category=cat1, rank=29,
    photo_attribution="F. Genevey [CC BY-SA 3.0 (http://creativecommons.org/"
                      "licenses/by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/2/2a/"
          "Cockeramericain1.jpg")
session.add(breed7)
session.commit()

breed8 = Breed(
    name="Vizsla",
    description="The Vizsla is a versatile, red-coated gundog built for "
                "long days in the field. For centuries, these rugged but "
                "elegant athletes have been the pride of Hungarian sportsmen "
                "and their popularity in America increases with each passing "
                "year.",
    category=cat1, rank=30,
    photo_attribution="Darrel Birkett [CC BY 2.0 (https://creativecommons.org/"
                      "licenses/by/2.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/f/f9/"
          "Hungarian_Vizsla.jpg")
session.add(breed8)
session.commit()

breed9 = Breed(
    name="Weimaraner",
    description="The Weimaraner, Germany's sleek and swift \"Gray Ghost,\" "
                "is beloved by hunters and pet owners alike for their "
                "friendliness, obedience, and beauty. They enjoy exercise, "
                "and plenty of it, along with lots of quality time with "
                "their humans.",
    category=cat1, rank=34,
    photo_attribution="Mike Bostock [CC BY-SA 2.0 ("
                      "https://creativecommons.org/licenses/by-sa/2.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/6/66/"
          "Weimaraner_barking.jpg")
session.add(breed9)
session.commit()

# Hound Group
cat2 = Category(name="Hound")
session.add(cat2)
session.commit()

breed1 = Breed(
    name="Beagle",
    description="Not only is the Beagle an excellent hunting dog and loyal "
                "companion, it is also happy-go-lucky, funny, and - thanks "
                "to its pleading expression - cute. They were bred to hunt "
                "in packs, so they enjoy company and are generally "
                "easygoing.",
    category=cat2, rank=6,
    photo_attribution="Taz80 / SEDIRI Eddy [CC BY-SA 3.0 ("
                      "https://creativecommons.org/licenses/by-sa/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/b/b7/"
          "Beagle_Faraon.JPG")
session.add(breed1)
session.commit()

breed2 = Breed(
    name="Dachshund",
    description="The famously long, low silhouette, ever-alert expression, "
                "and bold, vivacious personality of the Dachshund have made "
                "him a superstar of the canine kingdom. Dachshunds come in "
                "two sizes and in three coat types of various colors and "
                "patterns.",
    category=cat2, rank=13,
    photo_attribution="Igor Bredikhin [CC BY 3.0 ("
                      "https://creativecommons.org/licenses/by/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/2/27/"
          "Short-haired-Dachshund.jpg")
session.add(breed2)
session.commit()

breed3 = Breed(
    name="Basset Hound",
    description="Among the most appealing of the AKC breeds, the endearing "
                "and instantly recognizable Basset Hound is a perennial "
                "favorite of dog lovers all over the world. This low-slung "
                "and low-key hound can be sometimes stubborn, but is always "
                "charming.",
    category=cat2, rank=39,
    photo_attribution="Bonnie van den Born, http://www.bonfoto.nlCwazi at "
                      "nl.wikipedia [CC BY-SA 3.0 ("
                      "http://creativecommons.org/licenses/by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/2/2a/"
          "Bvdb-bassethound2.jpg")
session.add(breed3)
session.commit()

breed4 = Breed(
    name="Rhodesian Ridgeback",
    description="The Rhodesian Ridgeback is an all-purpose \"Renaissance "
                "hound\" whose hallmark is the ridge, or stripe of backward-"
                "growing hair, on his back. Though the breed was made famous "
                "in its native Africa for its skill at tracking and baying - "
                "but never, ever killing - lions, today Ridgebacks are "
                "cherished family dogs whose owners must be prepared to "
                "deal with their independence and strong prey drive.",
    category=cat2, rank=41,
    photo_attribution="Dana.weignerova [CC BY-SA 3.0 ("
                      "https://creativecommons.org/licenses/by-sa/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/4/4e/"
          "Rhodesian_ridgeback2.jpg")
session.add(breed4)
session.commit()

breed5 = Breed(
    name="Bloodhound",
    description="The world famous \"Sleuth Hound\" does one thing better "
                "than any creature on earth: find people who are lost or "
                "hiding. An off-duty Bloodhound is among the canine "
                "kingdom's most docile citizens, but he's relentless and "
                "stubborn on scent.",
    category=cat2, rank=50,
    photo_attribution="Claudia Krebs, modyfikacja Pleple2000 [CC BY-SA 3.0 ("
                      "http://creativecommons.org/licenses/by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/c/c6/"
          "Bloodhound_800.jpg")
session.add(breed5)
session.commit()

# Working Group
cat3 = Category(name="Working")
session.add(cat3)
session.commit()

breed1 = Breed(
    name="Rottweiler",
    description="The Rottweiler is a robust working breed of great strength "
                "descended from the mastiffs of the Roman legions. A gentle "
                "playmate and protector within the family circle, the Rottie "
                "observes the outside world with a self-assured aloofness.",
    category=cat3, rank=8,
    photo_attribution="JUAN RAMON RODRIGUEZ SOSA [CC BY-SA 2.0 ("
                      "https://creativecommons.org/licenses/by-sa/2.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/f/fb/02_I_Exposici"
          "%C3%B3n_Monogr%C3%A1fica_Club_Rottweiler_de_Espa%C3%B1a_-_"
          "Santa_Brigida_-_Gran_Canaria.jpg")
session.add(breed1)
session.commit()

breed2 = Breed(
    name="Boxer",
    description="Loyalty, affection, intelligence, work ethic, and good "
                "looks: Boxers are the whole doggy package. Bright and "
                "alert, sometimes silly, but always courageous, the Boxer "
                "has been among America's most popular dog breeds for a "
                "very long time.",
    category=cat3, rank=11,
    photo_attribution="AnonymousUnknown author [CC BY-SA 3.0 ("
                      "https://creativecommons.org/licenses/by-sa/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/8/8c/Boxer.jgp.jpg")
session.add(breed2)
session.commit()

breed3 = Breed(
    name="Siberian Husky",
    description="The Siberian Husky, a thickly coated, compact sled dog of "
                "medium size and great endurance, was developed to work in "
                "packs, pulling light loads at moderate speeds over vast "
                "frozen expanses. Huskies are friendly, fastidious, and "
                "dignified.",
    category=cat3, rank=12,
    photo_attribution="Utopialand [CC BY-SA 4.0 ("
                      "https://creativecommons.org/licenses/by-sa/4.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/c/ca/"
          "Siberian-husky.jpg")
session.add(breed3)
session.commit()

breed4 = Breed(
    name="Great Dane",
    description="The easygoing Great Dane, the mighty \"Apollo of Dogs,\" is "
                "a total joy to live with - but owning a dog of such "
                "imposing size, weight, and strength is a commitment not to "
                "be entered into lightly. This breed is indeed great, but "
                "not a Dane.",
    category=cat3, rank=14,
    photo_attribution="Dogues Allemands de Jirova [CC BY-SA 4.0 ("
                      "https://creativecommons.org/licenses/by-sa/4.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/0/02/Korros_2.jpg")
session.add(breed4)
session.commit()

breed5 = Breed(
    name="Doberman Pinscher",
    description="Sleek and powerful, possessing both a magnificent physique "
                "and keen intelligence, the Doberman Pinscher is one of "
                "dogkind's noblemen. This incomparably fearless and vigilant "
                "breed stands proudly among the world's finest protection "
                "dogs.",
    category=cat3, rank=16,
    photo_attribution="Andreas Kollegger from Baltimore [CC BY 2.0 ("
                      "https://creativecommons.org/licenses/by/2.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/0/0c/"
          "Doberman_Pinscher_blue_portrait.jpg")
session.add(breed5)
session.commit()

breed6 = Breed(
    name="Bernese Mountain Dog",
    description="Big, powerful, and built for hard work, the Bernese "
                "Mountain Dog is also strikingly beautiful and blessed with "
                "a sweet, affectionate nature. Berners are generally placid "
                "but are always up for a romp with the owner, whom they live "
                "to please.",
    category=cat3, rank=25,
    photo_attribution="Ganjo  http://fr.wikipedia.org/wiki/Utilisateur:"
                      "Ganjo [CC BY-SA 3.0 (http://creativecommons.org/"
                      "licenses/by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/d/d4/"
          "Bouviers_Bernois_Ganjo.jpg")
session.add(breed6)
session.commit()

breed7 = Breed(
    name="Mastiff",
    description="The colossal Mastiff belongs to a canine clan as ancient as "
                "civilization itself. A massive, heavy-boned dog of courage "
                "and prodigious strength, the Mastiff is docile and "
                "dignified but also a formidable protector of those they "
                "hold dear.",
    category=cat3, rank=28,
    photo_attribution="Michelleparlier [CC BY-SA 3.0 ("
                      "https://creativecommons.org/licenses/by-sa/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/7/79/AM.Suma.jpg")
session.add(breed7)
session.commit()

breed8 = Breed(
    name="Newfoundland",
    description="The massive Newfoundland is a strikingly large, powerful "
                "working dog of heavy bone and dignified bearing. The sweet-"
                "tempered Newfie is a famously good companion and has earned "
                "a reputation as a patient and watchful \"nanny dog\" for "
                "kids.",
    category=cat3, rank=36,
    photo_attribution="SKern [CC BY-SA 3.0 ("
                      "http://creativecommons.org/licenses/by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/e/e0/"
          "Newfoundland_brown.jpg")
session.add(breed8)
session.commit()

breed9 = Breed(
    name="Cane Corso",
    description="Smart, trainable, and of noble bearing, the assertive and "
                "confident Cane Corso is a peerless protector. The Corso's "
                "lineage goes back to ancient Roman times, and the breed's "
                "name roughly translates from the Latin as \"bodyguard "
                "dog.\"",
    category=cat3, rank=37,
    photo_attribution="Kumarrrr [CC BY-SA 3.0 (http://creativecommons.org/"
                      "licenses/by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/3/37/"
          "CaneCorso_%2823%29.jpg")
session.add(breed9)
session.commit()

breed10 = Breed(
    name="Akita",
    description="Akita is muscular, double-coated dogs of ancient Japanese "
                "lineage famous for her dignity, courage, and loyalty. In "
                "her native land, she's venerated as family protectors and "
                "symbols of good health, happiness, and long life.",
    category=cat3, rank=47,
    photo_attribution="B@rt at the Dutch language Wikipedia ["
                      "CC BY-SA 3.0 (http://creativecommons.org/licenses/"
                      "by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/7/78/"
          "Akita_inu.jpeg")
session.add(breed10)
session.commit()

breed11 = Breed(
    name="St. Bernard",
    description="The Saint Bernard does not rank very high in AKC "
                "registrations, but the genial giant of the Swiss Alps is "
                "nonetheless among the world's most famous and beloved "
                "breeds. Saints are famously watchful and patient \"nanny "
                "dogs\" for children.",
    category=cat3, rank=48,
    photo_attribution="Cassie J [CC BY 2.0 ("
                      "https://creativecommons.org/licenses/by/2.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/f/f6/"
          "St_Bernard_Dog_001.jpg")
session.add(breed11)
session.commit()

# Terrier Group
cat4 = Category(name="Terrier")
session.add(cat4)
session.commit()

breed1 = Breed(
    name="Miniature Schnauzer",
    description="The Miniature Schnauzer, the smallest of the three "
                "Schnauzer breeds, is a generally healthy, long-lived, and "
                "low-shedding companion. Add an outgoing personality, a "
                "portable size, and sporty good looks, and you've got an "
                "ideal family dog.",
    category=cat4, rank=18,
    photo_attribution="I, Lilly M [CC BY-SA 3.0 ("
                      "http://creativecommons.org/licenses/by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/4/47/"
          "Miniature_Schnauzer_R_02.JPG")
session.add(breed1)
session.commit()

breed2 = Breed(
    name="West Highland White Terrier",
    description="Smart, confident, and always entertaining at play, the "
                "adorable West Highland White Terrier (Westie, for short) "
                "has charmed owners for over 300 years. This diminutive but "
                "sturdy earthdog is among the most popular of the small "
                "terriers.",
    category=cat4, rank=42,
    photo_attribution="Imoen [CC BY-SA 3.0 ("
                      "http://creativecommons.org/licenses/by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/e/ec/"
          "West_Highland_White_Terrier.JPG")
session.add(breed2)
session.commit()

breed3 = Breed(
    name="Soft Coated Wheaten Terrier",
    description="The Soft Coated Wheaten Terrier, an exuberant Irish farm "
                "dog, is happy, friendly, deeply devoted, and just stubborn "
                "enough to remind you he's a terrier. The unique wheaten "
                "coat is low-shedding but needs diligent care to avoid "
                "matting.",
    category=cat4, rank=49,
    photo_attribution="Terrierk&auml;nnaren [CC BY-SA 3.0 ("
                      "https://creativecommons.org/licenses/by-sa/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/f/fd/"
          "Soft-Coated_Wheaten_Terrier.jpg")
session.add(breed3)
session.commit()

# Toy Group
cat5 = Category(name="Toy")
session.add(cat5)
session.commit()

breed1 = Breed(
    name="Yorkshire Terrier",
    description="Beneath the dainty, glossy, floor-length coat of a "
                "Yorkshire Terrier beats the heart of a feisty, old-time "
                "terrier. Yorkies earned their living as ratters in mines "
                "and mills long before they became the beribboned lapdogs of "
                "Victorian ladies.",
    category=cat5, rank=9,
    photo_attribution="Pelz [CC BY-SA 3.0 ("
                      "https://creativecommons.org/licenses/by-sa/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/1/13/"
          "Filou_DSC01224_ji.jpg")
session.add(breed1)
session.commit()

breed2 = Breed(
    name="Cavalier King Charles Spaniel",
    description="The Cavalier King Charles Spaniel wears his connection to "
                "British history in his breed's name. Cavaliers are the best "
                "of two worlds, combining the gentle attentiveness of a toy "
                "breed with the verve and athleticism of a sporting spaniel.",
    category=cat5, rank=19,
    photo_attribution="Mapovfille [CC BY 3.0 ("
                      "https://creativecommons.org/licenses/by/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/a/ab/"
          "Betty_Verdure.Photo_Ph.BRIZARD.JPG")
session.add(breed2)
session.commit()

breed3 = Breed(
    name="Shih Tzu",
    description="That face! Those big dark eyes looking up at you with that "
                "sweet expression! It's no surprise that Shih Tzu owners "
                "have been so delighted with this little \"Lion Dog\" for a "
                "thousand years. Where Shih Tzu go, giggles and mischief "
                "follow.",
    category=cat5, rank=20,
    photo_attribution="Melanie Dullinger - White Magic Kennels "
                      "&lt;info@whitemagickennels.com&gt; [CC BY-SA 3.0 ("
                      "http://creativecommons.org/licenses/by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/3/30/Shih-Tzu.JPG")
session.add(breed3)
session.commit()

breed4 = Breed(
    name="Pomeranian",
    description="The tiny Pomeranian, long a favorite of royals and "
                "commoners alike, has been called the ideal companion. The "
                "glorious coat, smiling, foxy face, and vivacious "
                "personality have helped make the Pom one of the world's "
                "most popular toy breeds.",
    category=cat5, rank=22,
    photo_attribution="Rob Hanson [CC BY 2.0 ("
                      "https://creativecommons.org/licenses/by/2.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/c/cb/"
          "Pomeranian_orange-sable_Coco.jpg")
session.add(breed4)
session.commit()

breed5 = Breed(
    name="Havanese",
    description="Havanese, the only dog breed native to Cuba, are cheerful "
                "little dogs with a spring in their step and a gleam in "
                "their big, brown eyes. These vivacious and sociable "
                "companions are becoming especially popular with American "
                "city dwellers.",
    category=cat5, rank=23,
    photo_attribution="audrey_sel [CC BY-SA 2.0 ("
                      "https://creativecommons.org/licenses/by-sa/2.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/e/ed/"
          "A_Havanese_judging.jpg")
session.add(breed5)
session.commit()

breed6 = Breed(
    name="Pug",
    description="Once the mischievous companion of Chinese emperors, and "
                "later the mascot of Holland's royal House of Orange, the "
                "small but solid Pug is today adored by his millions of fans "
                "around the world. Pugs live to love and to be loved in "
                "return.",
    category=cat5, rank=31,
    photo_attribution="Cwazi at Dutch Wikipedia(Original text: Bonnie van "
                      "den Born, http://www.bonfoto.nl) [CC BY-SA 3.0 ("
                      "http://creativecommons.org/licenses/by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/4/48/"
          "Mopshond2_03-10-2005.jpg")
session.add(breed6)
session.commit()

breed7 = Breed(
    name="Chihuahua",
    description="The Chihuahua is a tiny dog with a huge personality. A "
                "national symbol of Mexico, these alert and amusing \"purse "
                "dogs\" stand among the oldest breeds of the Americas, with "
                "a lineage going back to the ancient kingdoms of "
                "pre-Columbian times.",
    category=cat5, rank=32,
    photo_attribution="Tatiana Borisova [CC BY-SA 3.0 ("
                      "https://creativecommons.org/licenses/by-sa/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/6/65/"
          "Chihuahuasmoothcoat.jpg")
session.add(breed7)
session.commit()

breed8 = Breed(
    name="Maltese",
    description="The tiny Maltese, \"Ye Ancient Dogge of Malta,\" has been "
                "sitting in the lap of luxury since the Bible was a work in "
                "progress. Famous for their show-stopping, floor-length "
                "coat, Maltese are playful, charming, and adaptable toy "
                "companions.",
    category=cat5, rank=33,
    photo_attribution="SheltieBoy [CC BY 2.0 ("
                      "https://creativecommons.org/licenses/by/2.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/c/cc/"
          "01_AKC_Maltese_Dog_Show_2013.jpg")
session.add(breed8)
session.commit()

# Non-Sporting Group
cat6 = Category(name="Non-Sporting")
session.add(cat6)
session.commit()

breed1 = Breed(
    name="French Bulldog",
    description="The one-of-a-kind French Bulldog, with his large bat ears "
                "and even disposition, is one of the world's most popular "
                "small-dog breeds, especially among city dwellers. The "
                "Frenchie is playful, alert, adaptable, and completely "
                "irresistible.",
    category=cat6, rank=4,
    photo_attribution="The original uploader was EGILEO at Italian "
                      "Wikipedia. [CC BY 2.0 ("
                      "https://creativecommons.org/licenses/by/2.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/2/2f/Bou.jpg")
session.add(breed1)
session.commit()

breed2 = Breed(
    name="Bulldog",
    description="Kind but courageous, friendly but dignified, the Bulldog is "
                "a thick-set, low-slung, well-muscled bruiser whose "
                "\"sourmug\" face is the universal symbol of courage and "
                "tenacity. These docile, loyal companions adapt well to "
                "town or country.",
    category=cat6, rank=5,
    photo_attribution="Quizillafreak [CC BY-SA 3.0 ("
                      "https://creativecommons.org/licenses/by-sa/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/e/eb/"
          "White-red_English_bulldog.jpg")
session.add(breed2)
session.commit()

breed3 = Breed(
    name="Poodle (Miniature/Standard)",
    description="Whether Standard, Miniature, or Toy, and either black, "
                "white, or apricot, the Poodle stands proudly among dogdom's "
                "true aristocrats. Beneath the curly, hypoallergenic coat is "
                "an elegant athlete and companion for all reasons and "
                "seasons.",
    category=cat6, rank=7,
    photo_attribution="John Leslie from London, UK [CC BY 2.0 ("
                      "https://creativecommons.org/licenses/by/2.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/e/e2/"
          "Standard_poodle_apricot.jpg")
session.add(breed3)
session.commit()

breed4 = Breed(
    name="Boston Terrier",
    description="The Boston Terrier is a lively little companion recognized "
                "by his tight tuxedo jacket, sporty but compact body, and "
                "the friendly glow in his big, round eyes. His impeccable "
                "manners have earned him the nickname \"The American "
                "Gentleman.\"",
    category=cat6, rank=21,
    photo_attribution="The original uploader was Elf at English Wikipedia. ["
                      "CC BY-SA 3.0 ("
                      "http://creativecommons.org/licenses/by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/6/66/"
          "BostonTerrierBrindleStand_w.jpg")
session.add(breed4)
session.commit()

breed5 = Breed(
    name="Shiba Inu",
    description="An ancient Japanese breed, the Shiba Inu is a little but "
                "well-muscled dog once employed as a hunter. Today, the "
                "spirited, good-natured Shiba is the most popular companion "
                "dog in Japan. The adaptable Shiba is at home in town or "
                "country.",
    category=cat6, rank=45,
    photo_attribution="Yozakura [Public domain]",
    photo="https://upload.wikimedia.org/wikipedia/commons/2/20/Shiba_Inu.jpg")
session.add(breed5)
session.commit()

breed6 = Breed(
    name="Bichon Frise",
    description="The small but sturdy and resilient Bichon Frise stands "
                "among the world's great \"personality dogs.\" Since "
                "antiquity, these irresistible canine comedians have relied "
                "on charm, beauty, and intelligence to weather history's ups "
                "and downs.",
    category=cat6, rank=46,
    photo_attribution="Editor at Large [CC BY-SA 2.5 ("
                      "https://creativecommons.org/licenses/by-sa/2.5)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/c/c5/"
          "Bichon_Frise.jpg")
session.add(breed6)
session.commit()


# Herding Group
cat7 = Category(name="Herding")
session.add(cat7)
session.commit()

breed1 = Breed(
    name="German Shepherd",
    description="Generally considered dogkind\'s finest all-purpose worker, "
                "the German Shepherd Dog is a large, agile, muscular dog of "
                "noble character and high intelligence. Loyal, confident, "
                "courageous, and steady, the German Shepherd is truly a dog "
                "lover\'s delight.",
    category=cat7, rank=2,
    photo_attribution="Dario Sgroi [CC BY-SA 3.0 ("
                      "https://creativecommons.org/licenses/by-sa/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/9/94/"
          "Cane_da_pastore_tedesco_adulto.jpg")
session.add(breed1)
session.commit()

breed2 = Breed(
    name="Pembroke Welsh Corgi",
    description="Among the most agreeable of all small housedogs, the "
                "Pembroke Welsh Corgi is a strong, athletic, and lively "
                "little herder who is affectionate and companionable without "
                "being needy. They are one the world's most popular herding "
                "breeds.",
    category=cat7, rank=15,
    photo_attribution="Pmuths1956 [CC BY-SA 3.0 ("
                      "https://creativecommons.org/licenses/by-sa/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/f/fb/"
          "Welchcorgipembroke.JPG")
session.add(breed2)
session.commit()

breed3 = Breed(
    name="Australian Shepherd",
    description="The Australian Shepherd, a lean, tough ranch dog, is one of "
                "those \"only in America\" stories: a European breed "
                "perfected in California by way of Australia. Fixtures on "
                "the rodeo circuit, they are closely associated with the "
                "cowboy life.",
    category=cat7, rank=17,
    photo_attribution="sannse [CC BY-SA 3.0 ("
                      "http://creativecommons.org/licenses/by-sa/3.0/)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/5/52/"
          "Australian_Shepherd_600.jpg")
session.add(breed3)
session.commit()

breed4 = Breed(
    name="Shetland Sheepdog",
    description="The Shetland Sheepdog, also known as the Sheltie, is an "
                "extremely intelligent, quick, and obedient herder from "
                "Scotland's remote and rugged Shetland Islands. Shelties "
                "bear a strong family resemblance to their bigger cousin, "
                "the Collie.",
    category=cat7, rank=24,
    photo_attribution="MBOE3 [CC BY-SA 3.0 ("
                      "https://creativecommons.org/licenses/by-sa/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/4/44/"
          "Mabel_Joy%27s_Heartbreaker.jpg")
session.add(breed4)
session.commit()

breed5 = Breed(
    name="Miniature American Shepherd",
    description="The Miniature American Shepherd resembles a small "
                "Australian Shepherd. True herders in spite of their compact "
                "size, Minis are bright, self-motivated workers and "
                "endearingly loyal and lively companion dogs who have an "
                "affinity for horses.",
    category=cat7, rank=35,
    photo_attribution="Lextergrace [CC BY-SA 4.0 ("
                      "https://creativecommons.org/licenses/by-sa/4.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/7/77/"
          "Blue_Merle_Miniature_American_Shepherd_in_Grass.jpg")
session.add(breed5)
session.commit()

breed6 = Breed(
    name="Border Collie",
    description="A remarkably bright workaholic, the Border Collie is an "
                "amazing dog - maybe a bit too amazing for owners without "
                "the time, energy, or means to keep it occupied. These "
                "energetic dogs will settle down for cuddle time when the "
                "workday is done.",
    category=cat7, rank=38,
    photo_attribution="Lenkahol at Czech Wikipedia [Public domain]",
    photo="https://upload.wikimedia.org/wikipedia/commons/6/65/"
          "Borderkolie.jpg")
session.add(breed6)
session.commit()

breed7 = Breed(
    name="Collie",
    description="The majestic Collie, thanks to a hundred years as a pop-"
                "culture star, is among the world's most recognizable and "
                "beloved dog breeds. The full-coated \"rough\" Collie is the "
                "more familiar variety, but there is also a sleek \"smooth\" "
                "Collie.",
    category=cat7, rank=40,
    photo_attribution="Ron Armstrong from Helena, MT, USA [CC BY 2.0 ("
                      "https://creativecommons.org/licenses/by/2.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/a/a6/"
          "Rough_Collie_agility_jump.jpg")
session.add(breed7)
session.commit()

breed8 = Breed(
    name="Belgian Malinois",
    description="The smart, confident, and versatile Belgian Malinois is a "
    "world-class worker who forges an unbreakable bond with his human "
    "partner. To deny a Mal activity and the pleasure of your company is to "
    "deprive him of his very reasons for being.",
    category=cat7, rank=44,
    photo_attribution="Canarian [CC BY-SA 3.0 ("
                      "https://creativecommons.org/licenses/by-sa/3.0)]",
    photo="https://upload.wikimedia.org/wikipedia/commons/7/7b/"
          "Malinois_Shepherd3.JPG")
session.add(breed8)
session.commit()


print "added dog breeds!"
