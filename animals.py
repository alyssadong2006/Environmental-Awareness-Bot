import random

Africa = [
  [
    'Ethiopian Wolf',
    'The Ethiopian wolf is Africa\’s most endangered carnivore and the continent\’s only wolf species. It is a handsome rusty red jackal-like dog and, as the name suggests, it is endemic to Ethiopia\’s  It is endangered due to loss of habitat to farmland and due to diseases caught from domestic dogs.',
    'AnimalPic/Ethiopian Wolf.gif'
  ],
  [
    'Pangolin',
    'The poor pangolin has the dubious honor of being the most illegally trafficked species in Africa, as its scales are used in traditional medicine in Asia. Most people have never heard of a pangolin, let alone seen one … and sadly it is feared they are on a fast-track to extinction. Pangolins are now one of the most endangered animals in Africa. These delightful, gentle creatures are armour-plated and roll into a ball to defend themselves \– unfortunately a poor defence against humans. Pangolins feed on ants and termites with their long sticky tongues, and the mother carries her young infant on her back. They are the holy grail of wildlife sightings for many tourists and indeed safari guides, such is their rarity.',
    'AnimalPic/Pangolin.gif'
  ],
  [
    'Black Rhino',
    'Black rhinos are actually grey in color and are distinguished from white rhinos by their pointed, prehensile upper lip, whereas white rhinos have square lips. Black rhino calves usually follow their mother \– whereas white rhino calves often trot along in front.  Black rhinos are largely solitary and are browsers rather than grazers \– hence their hooked lip. Black rhinos are classified as Critically Endangered, as they have been decimated by poaching for their horn. The most recent numbers estimate less than 5000 in 2010, however, numbers are likely to have decreased further since then, despite valiant conservation efforts.',
    'AnimalPic/Black Rhino.jpg'
  ],
  [
    'White Rhino',
    'It is sad that, after successful conservation efforts increased their numbers dramatically in the 1960\’s, once again, white rhino has become one of the most endangered animals in Africa. This is due to illegal poaching to satisfy the increased demand for their horn by Asian markets. Valiant conservation efforts are once again underway to save the white rhino, and South Africa is still its stronghold. The white rhino is larger than the black rhino and has square lips for grazing.',
    'AnimalPic/White Rhino.jpg'
  ],
  [
    'Mountain Gorilla',
    'Although mountain gorillas are still considered one of the most endangered animals in Africa, the good news is that their numbers are actually on the increase. An encounter with mountain gorillas should be on everyone\’s bucket list.',
    'AnimalPic/Mountain Gorilla.gif'
  ],
  [
    'African Wild Dog',
    'Previously viewed as vermin, thankfully the African wild dog has had a very good PR makeover over the last few years and has now become one of the most wished-for safari sightings. Sightings on safari are often by luck, as the dogs cover huge distances in search of prey, and it is only when they are denning (usually the dry season months) that they remain in the same place for a few weeks.',
    'AnimalPic/African Wild Dog.gif'
  ],
  [
    'African Penguin',
    'For visitors to Cape Town, it is hard to imagine that the African penguin is one of the most endangered species in Africa. They are easy to see at Boulders Bay on the Cape Peninsula, where there is a visitor centre and boardwalk past their nests. However, sadly, African penguin numbers have plummeted in recent years due to depleted fish stocks from over fishing and fish stocks moving further west due to climate change. The African penguin is also at risk from oil spills.',
    'AnimalPic/African Penguin.gif'
  ],
  [
    'Rothschild\’s Giraffe',
    'The giraffe is one of Africa\’s most recognisable and iconic animals and the tallest land mammal. While giraffes are commonly seen on safari, people are unaware that the numbers of these majestic animals are crashing dramatically outside of protected areas due to habitat loss, illegal hunting and human-wildlife conflict. There are nine subspecies of giraffe, each confined to specific regions of Africa. The Rothschild\’s giraffe is now listed as one of the most endangered animals in Africa \– in 2010 there were thought to be less than 670 individuals.',
    'AnimalPic/Rothschild’s Giraffe.gif'
  ],
  [
    'Hooded Vulture',
    'Vultures are a critical component in the African landscape but their numbers are plummeting due to increased poisoning incidents. Without vultures clearing carcasses, there is a risk in the increase of disease \– as has happened in India, where they have lost 95% of their vultures. The hooded vulture is now one of the most endangered species in Africa \– recently upgraded to Critically Endangered. They are easy to distinguish from other vultures by their small size and thin hooked bill.',
    'AnimalPic/Hooded Vulture.jpg'
  ],
  [
    'Chimpanzee',
    'When you look into the eyes of a wild chimpanzee, it is easy to understand that this is man\’s closest relative \– we share 98% of the same genes. Their behavior is distinctively human-like too. Tracking chimpanzees in the wild is one of the most exciting safari activities \– it really does feel like you are in the middle of your very own wildlife documentary. Chimpanzees are classified as one of the most endangered animals in Africa \– the biggest threat to their survival is habitat loss and an increasing demand for bushmeat.',
    'AnimalPic/Chimpanzee.jpg'
  ]
]

#source: https://www.safaribookings.com/blog/endangered-animals-africa

Antartica = [
  [
    'Emperor penguins',
    'Emperor penguins now a threatened species due to climate change, U.S. says. Antarctica\'s emperor penguin is at risk of extinction due to rising global temperatures and sea ice loss, the U.S. government said, as it gave the bird new protections under its Endangered Species Act.',
    'AnimalPic/Emperor Penguins.gif'
  ],
  [
    'Antarctic krill',
    'They play an important role in the aquatic food chain, particularly in the Southern Ocean. Antarctic krill provide a vital food source for whales, seals, ice fish, and penguins. These animals depend on eating large quantities of krill for survival in the harsh climate.',
    'AnimalPic/Antarctic krill.gif'
  ],
  [
    'Sperm Whale',
    'Sperm whales were a primary target of the commercial whaling industry from 1800 to 1987, which nearly decimated all sperm whale populations.',
    'AnimalPic/Sperm Whale.gif'
  ],
  [
    'Sei Whale',
    'The largest threat to the Sei Whale is the lack of recovery in their population, which declined when commercial whaling was still legal in Canada. \n\nThere are also many factors that could be indirectly affecting the Sei Whale population. These include habitat loss due to commercial fishing, noise and traffic from boats, and contamination from chemicals. \n\nSei Whales are also at risk due to climate change, pollution, and being hit by ships. They can also become tangled in fishing nets and gear.',
    'AnimalPic/Sei Whale.gif'
  ]
]

#source
#https://www.cbc.ca/news/science/emperor-penguins-threatened-climate-change-1.6629076#:~:text=Science-,Emperor%20penguins%20now%20a%20threatened%20species%20due%20to%20climate%20change,under%20its%20Endangered%20Species%20Act.
#https://oceantoday.noaa.gov/animalsoftheice_krill/#:~:text=They%20play%20an%20important%20role,survival%20in%20the%20harsh%20climate.
#https://www.fisheries.noaa.gov/species/sperm-whale#:~:text=Sperm%20whales%20were%20a%20primary,decimated%20all%20sperm%20whale%20populations.
#https://naturecanada.ca/discover-nature/endangered-species/sei-whale/

Asia = [
  [
    'Snow Leopard',
    'The elegant and well-camouflaged snow leopard is one of the world\'s most elusive cats. Thinly spread across 12 countries in central Asia, it\'s at home in high, rugged mountain landscapes. But habitat deterioration, habitat loss, poaching and climate change are now threatening their survival.',
    'AnimalPic/Snow Leapord.gif'
  ],
  [
    'Tiger',
    'Tigers have lost an estimated 95% of their historical range. Their habitat has been destroyed, degraded, and fragmented by human activities. The clearing of forests for agriculture and timber, as well as the building of road networks and other development activities, pose serious threats to tiger habitats.',
    'AnimalPic/Tiger.gif'
  ],
  [
    'Giant Panda',
    'Infrastructure development (such as dams, roads, and railways) is increasingly fragmenting and isolating panda populations, preventing pandas from finding new bamboo forests and potential mates. Forest loss also reduces pandas\' access to the bamboo they need to survive.',
    'AnimalPic/Giant Panda.gif'
  ],
  [
    'Rhinoceros',
    'Very few rhinos survive outside national parks and reserves due to persistent poaching and habitat loss over many decades. Three species of rhino—black, Javan, and Sumatran—are critically endangered.',
    'AnimalPic/Rhinoceros.gif'
  ]
]

#source:
#https://www.wwf.org.uk/learn/wildlife/snow-leopards#:~:text=The%20elegant%20and%20well%2Dcamouflaged,are%20now%20threatening%20their%20survival.
#https://www.worldwildlife.org/species/tiger#:~:text=Tigers%20have%20lost%20an%20estimated,serious%20threats%20to%20tiger%20habitats.
#https://www.worldwildlife.org/species/giant-panda#:~:text=Infrastructure%20development%20(such%20as%20dams,bamboo%20they%20need%20to%20survive.
#https://www.worldwildlife.org/species/rhino#:~:text=Very%20few%20rhinos%20survive%20outside,and%20Sumatran%E2%80%94are%20critically%20endangered.

Europe = [
  [
    'European Mink',
    'The European mink (Mustela lutreola) is critically endangered and one of the most threatened mammals in Europe. Once widespread across Europe, the European mink population has undergone a severe decline and now occupies less than 20% of its former range.',
    'AnimalPic/European Mink.jpg'
  ],
  [
    'Mediterranean monk seal',
    'Major threats to the Mediterranean monk seal include displacement and habitat deterioration, deliberate killing by humans, and fisheries bycatch and entanglement.',
    'AnimalPic/Mediterranean monk seal.jpg'
  ],
  [
    'The North Atlantic right whale',
    'By the 1890s, North Atlantic right whales were hunted to the brink of extinction by commercial whalers. Today, the leading causes of mortality are entanglement in fishing gear and vessel strikes. Over 80 per cent of North Atlantic right whales have been entangled at least once in their lifetime.',
    'AnimalPic/The North Atlantic right whale.gif'
  ],
  [
    'Polar Bear',
    'The Arctic is warming about twice as fast as the global average, causing the ice that polar bears depend on to melt away. Loss of sea ice also threatens the bear\'s main prey, seals, which need the ice to raise their young.',
    'AnimalPic/Polar Bear.gif'
  ]
]

#source:
#https://www.vwt.org.uk/species/european-mink/#:~:text=The%20European%20mink%20(Mustela%20lutreola,20%25%20of%20its%20former%20range.
#https://www.fisheries.noaa.gov/species/mediterranean-monk-seal#:~:text=Major%20threats%20to%20the%20Mediterranean,the%20coast%20of%20Northwest%20Africa.
#https://wwf.ca/species/north-atlantic-right-whales/#:~:text=By%20the%201890s%2C%20North%20Atlantic,least%20once%20in%20their%20lifetime.

Australia = [
  [
    'Numbat',
    'Numbats are small, striped marsupials that were once widespread across mainland Australia. Numbats declined to only about 300 individuals in WA by the late 1970s, primarily due to predation by foxes and habitat loss. Additional threats include predation by feral cats, and frequent and intense fires.',
    'AnimalPic/Numbat.gif'
  ],
  [
    'Gouldian Finch',
    'The greatest threats to Gouldian finches and other grass-eating birds are changes to habitat resulting from altered fire patterns and grazing pressure. research has shown that both fire and grazing can reduce the amount of wet season grass seed available to Gouldians.',
    'AnimalPic/Gouldian Finch.gif'
  ],
  [
    'Mountain Pygmy-possum',
    'The Mountain Pygmy-possum is threatened in NSW by the loss, degradation and fragmentation of habitat. Two of the four main sub-populations are located within ski resort areas. Past management practices by the resorts have led to direct loss of habitat and alteration of vegetation.',
    'AnimalPic/Mountain Pygmy-possum.jpg'
  ],
  [
    'Regent Honeyeater',
    'The Regent Honeyeater has been in decline since the 1940s, and its soft, metallic chiming call is rarely heard. The few remaining honeyeaters live along the east coast of Australia. They are no longer found in south-western Victoria, and are probably extinct in South Australia.',
    'AnimalPic/Regent Honeyeater.jpg'
  ],
  [
    'Woylie',
    'A Woylie is a member of the rat-kangaroo family, it moves by hopping and is active at night, digging for fungi to eat. It is also a marsupial and carries its young in a pouch. Predation by European foxes and more recently, feral cats, is the major cause of range contraction and decline of Woylie populations in Australia.',
    'AnimalPic/Woylie.gif'
  ]
]
#source
#https://www.dcceew.gov.au/environment/biodiversity/threatened/species/20-mammals-by-2020/numbat#:~:text=Numbats%20are%20small%2C%20striped%20marsupials,and%20frequent%20and%20intense%20fires.
#https://www.dcceew.gov.au/sites/default/files/documents/tsday08-gouldian-finch.pdf
#https://www.environment.nsw.gov.au/topics/animals-and-plants/threatened-species/nsw-threatened-species-scientific-committee/determinations/final-determinations/2000-2003/mountain-pygmy-possum-burramys-parvus-endangered-species-listing#:~:text=The%20Mountain%20Pygmy%2Dpossum%20is%20threatened%20in%20NSW%20by%20the,habitat%20and%20alteration%20of%20vegetation.
#https://www.zoo.org.au/fighting-extinction/local-threatened-species/regent-honeyeater/#:~:text=The%20Regent%20Honeyeater%20has%20been,probably%20extinct%20in%20South%20Australia.
#https://en.wikipedia.org/wiki/Woylie
#https://www.australianwildlife.org/wildlife/woylie-brush-tailed-bettong/#:~:text=Predation%20by%20European%20foxes%20and,fox%2Dbaiting%20during%20the%201980s.

America = [
  [
    'Florida Panther',
    'The Florida panther has been listed as an endangered species since 1967 and now lives in just 5% of its former range. This panther used to roam much of the southeastern U.S. but is now only found in southern Florida. There are only about 100 to 200 panthers left. They were heavily hunted and perceived as pests before being listed as endangered; today, their main threats are habitat loss and collisions with vehicles.',
    'AnimalPic/Florida Panther.jpg'
  ],
  [
    'Florida Manatee',
    'Boat strikes are a top threat to manatees, but climate change has caused caused problems for these gentle “sea cows.” Water temperature fluctuations put stress on the species, and increasing rates of deadly algal blooms are also to blame. In recent years, sea grass scarcity has led to starvation for these animals.',
    'AnimalPic/Florida Manatee.gif'
  ],
  [
    'Red Wolf',
    'There are only about 15 to 17 red wolves left in the wild in the U.S. In 1987, they were considered extinct, but a captive breeding program revived the species. Conservation efforts brought the population to over 100 animals around 2012, but by 2018, it dropped to 40 and now sits at less than two dozen.',
    'AnimalPic/Red Wolf.gif'
  ],
  [
    'California Condor',
    'California condors are the largest bird in North America. In the 1980s, California condors nearly went extinct due to poisoning from lead and consuming DDT, a pesticide that was banned in 1972. A successful captive breeding recovery program increased numbers from six to 223 in the early 2000s. Today, there are over 400 California condors, but they still are threatened by human-related deaths, such as collisions with power lines.',
    'AnimalPic/California Condor.gif'
  ],
  [
    'Black-Footed Ferret',
    'The only ferret species native to North America, there are only about 370 wild black-footed ferrets left in the wild. These creatures use prairie dog burrows across grasslands for their shelter, but increasing habitat loss due to agriculture has hurt the population. They eat prairie dogs, too, and prairie-dog eradication efforts have depleted their food source. They are also susceptible to diseases.',
    'AnimalPic/Black-Footed Ferret.gif'
  ],
  [
    'Loggerhead Sea Turtle',
    'Loggerhead sea turtles in the U.S. mostly call Florida\’s coasts home, but rapid development has been their downfall. Their nests, laid on beaches, are often destroyed, or they may be harrassed by humans while trying to nest. They are also often caught as bycatch by commercial fishers. These turtles are essential to healthy marine ecosystems, particularly coral reefs and seagrasses.',
    'AnimalPic/Loggerhead Sea Turtle.gif'
  ],
  [
    'San Joaquin Kit Fox',
    'San Joaquin kit foxes have suffered from habitat loss as land is turned into farms. Rodenticides, too, have led to population decline for these mammals. These kit foxes get much of their water from prey, but the smaller mammals they feed on have declined from pesticide use. The San Joaquin kit fox is the smallest fox in North America.',
    'AnimalPic/San Joaquin Kit Fox.jpg'
  ],
  [
    'Vaquita',
    'Vaquitas are the most endangered of the world\'s marine mammals. Less than 20 vaquitas remain in the wild, and entanglement in illegal gillnets is driving the species toward extinction',
    'Vaquita.jpg'
  ],
  [
    'Axolotls',
    'Despite being an important symbol of Mexican culture for centuries (they are named after Xolotl, the Aztec god of fire and lightning), axolotls have been under attack from various threats including rapid urbanization, pollution, invasive species and overfishing \– they are something of a delicacy in Mexico City.',
    'AnimalPic/Axolotls.gif'
  ]
]
#source
#https://www.ecowatch.com/most-endangered-animals-united-states.html
#https://www.fisheries.noaa.gov/species/vaquita#:~:text=Vaquitas%20are%20the%20most%20endangered,whale%2C%20dolphin%2C%20or%20porpoise.
#https://www.zurich.com/en/media/magazine/2020/it-isnt-too-late-to-save-the-axolotl#:~:text=And%20despite%20being%20an%20important,a%20delicacy%20in%20Mexico%20City.


def info(continent):
  if continent == 'africa':
    loc = Africa
  elif continent == 'antartica':
    loc = Antartica
  elif continent == 'asia':
    loc = Asia
  elif continent == 'europe':
    loc = Europe
  elif continent == 'australia':
    loc = Australia
  elif continent == 'america':
    loc = America

  animal = random.randint(0, len(loc) - 1)
  #this repeats two times, resulting in the animal value having diff values
  info_list = [f'**{loc[animal][0]}**\n{loc[animal][1]}', loc[animal][2]]
  return info_list
