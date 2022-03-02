# {{{ imports
from Component import Component
# }}}

# setup{{{

# T1 components{{{
toxic = Component('toxic')
chaosweaver = Component('chaosweaver')
frostweaver = Component('frostweaver')
permafrost = Component('permafrost')
hasted = Component('hasted')
deadeye = Component('deadeye')
bombardier = Component('bombardier')
flameweaver = Component('flameweaver')
incendiary = Component('incendiary')
arcane = Component('arcane')
echoist = Component('echoist')
stormweaver = Component('stormweaver')
dynamo = Component('dynamo')
bonebreaker = Component('bonebreaker')
bloodletter = Component('bloodletter')
steel = Component('steel')
gargantuan = Component('gargantuan')
berserker = Component('berserker')
sentinel = Component('sentinel')
juggernaut = Component('juggernaut')
vampiric = Component('vampiric')
overcharged = Component('overcharged')
soul = Component('soul')
opulent = Component('opulent')
malediction = Component('malediction')
consecrator = Component('consecrator')
frenzied = Component('frenzied')
# }}}

# t2 Components{{{

assassin = Component('assassin', backward=[deadeye, vampiric])
corruptor = Component('corruptor', backward=[bloodletter, chaosweaver])
drought = Component('drought', backward=[malediction, deadeye])
entangler = Component('entangler', backward=[toxic, bloodletter])
evocationist = Component('evocationist', backward=[flameweaver, frostweaver, stormweaver])
executioner = Component('executioner', backward=[frenzied, berserker])
flame_strider = Component('flame_strider',backward=[flameweaver,hasted])
frost_strider = Component('frost_strider',backward=[frostweaver,hasted])
storm_strider = Component('storm_strider',backward=[stormweaver,hasted])
heralding = Component('heralding',backward=[dynamo,arcane])
hexer = Component('hexer',backward=[chaosweaver,echoist])
ice_prison = Component('ice_prison',backward=[permafrost,sentinel])
invulnerable = Component('invulnerable',backward=[sentinel,juggernaut,consecrator])
magma = Component('magma',backward=[incendiary,bonebreaker])
mana = Component('mana',backward=[consecrator,dynamo])
mirror = Component('mirror',backward=[echoist,soul])
necromancer = Component('necromancer',backward=[bombardier,overcharged])
rejuvenating = Component('rejuvenating',backward=[gargantuan,vampiric])
treant = Component('treant',backward=[toxic,sentinel,steel])
# }}}

# t3 components{{{

abberath = Component('abberath',backward=[flame_strider,rejuvenating,frenzied])
brine = Component('brine',backward=[ice_prison,storm_strider,heralding])
corpse = Component('corpse',backward=[necromancer,incendiary])
crystal = Component('crystal',backward=[rejuvenating,permafrost,berserker])
effigy = Component('effigy',backward=[hexer,malediction,corruptor])
minions = Component('minions',backward=[necromancer,executioner,gargantuan])
elements = Component('elements',backward=[evocationist,steel,chaosweaver])
soul_eater = Component('soul_eater',backward=[necromancer,soul,gargantuan])
temporal = Component('temporal',backward=[hexer,juggernaut,arcane])
trickster = Component('trickster',backward=[assassin,overcharged,echoist])
tukohama = Component('tukohama',backward=[executioner,magma,bonebreaker])
# }}}

# t4 components{{{

arakali = Component('arakali',backward=[corruptor,entangler,assassin])
kitava = Component('kitava',backward=[abberath,corruptor,tukohama,corpse])
lunaris = Component('lunaris',backward=[invulnerable,minions,frost_strider])
shakari = Component('shakari',backward=[entangler,soul_eater,drought])
solaris = Component('solaris',backward=[invulnerable,magma,minions])
innocence = Component('innocence',backward=[lunaris,solaris,mirror,mana])
# }}}
# }}}

# forward assignments{{{

# t1{{{
toxic.forward = [entangler,treant]
chaosweaver.forward = [hexer,corruptor,elements]
frostweaver.forward = [frost_strider,evocationist]
permafrost.forward = [ice_prison,crystal]
hasted.forward = [frost_strider,flame_strider,storm_strider]
deadeye.forward = [assassin,drought]
bombardier.forward = [necromancer]
flameweaver.forward = [flame_strider,evocationist]
incendiary.forward = [corpse,magma]
arcane.forward = [heralding,temporal]
echoist.forward = [trickster,hexer,mirror]
stormweaver.forward = [evocationist,storm_strider]
dynamo.forward = [heralding,mana]
bonebreaker.forward = [magma,tukohama]
bloodletter.forward = [corruptor,entangler]
steel.forward = [treant,elements]
gargantuan.forward = [minions,rejuvenating, soul_eater]
berserker.forward = [executioner,crystal]
sentinel.forward = [treant,ice_prison,invulnerable]
juggernaut.forward = [invulnerable,temporal]
vampiric.forward = [assassin,rejuvenating]
overcharged.forward = [trickster,necromancer]
soul.forward = [soul_eater,mirror]
opulent.forward = None
malediction.forward = [drought,effigy]
consecrator.forward = [mana,invulnerable]
frenzied.forward = [abberath,executioner]
# }}}

# t2{{{
assassin.forward = [arakali,trickster]
corruptor.forward = [kitava,effigy]
drought.forward = [shakari]
entangler.forward = [arakali,shakari]
evocationist.forward = [elements]
executioner.forward = [tukohama,minions]
flame_strider.forward = [abberath]
frost_strider.forward = [lunaris]
storm_strider.forward = [brine]
heralding.forward = [brine]
hexer.forward = [temporal,effigy]
ice_prison.forward = [brine]
invulnerable.forward = [lunaris,solaris]
magma.forward = [tukohama,solaris]
mana.forward = [innocence]
mirror.forward = [innocence]
necromancer.forward = [minions,soul_eater,corpse]
rejuvenating.forward = [crystal,abberath]
treant.forward = None
# }}}

# t3{{{
abberath.forward = [kitava]
brine.forward = None
corpse.forward = [arakali,kitava]
crystal.forward = None
effigy.forward = None
minions.forward = [lunaris,soul_eater]
elements.forward = None
soul_eater.forward = [shakari]
temporal.forward = None
trickster.forward = None
tukohama.forward = [kitava]
# }}}

#{{{ t4
arakali.forward = None
kitava.forward = None
lunaris.forward = [innocence]
shakari.forward = None
solaris.forward = [innocence]
innocence.forward = None
# }}}

# }}}

# recipes

phat_uniques = Component('phat_uniques',backward=[treant,shakari,brine,tukohama],forward=None)


tier1 = [toxic, chaosweaver, frostweaver,permafrost,hasted,deadeye,bombardier,flameweaver,
         incendiary,arcane,echoist,stormweaver,dynamo,bonebreaker,bloodletter,steel,gargantuan,
         berserker,sentinel,juggernaut,vampiric,overcharged,soul,opulent,malediction,consecrator,
         frenzied]

tier2 = [assassin,corruptor,drought,entangler,evocationist,executioner,flame_strider,frost_strider,
         storm_strider,heralding,hexer,ice_prison,invulnerable,magma,mana,mirror,necromancer,
         rejuvenating,treant]

tier3 = [abberath,brine,corpse,crystal,effigy,minions,elements,soul_eater,
        temporal,trickster,tukohama]

tier4 = [arakali,kitava,lunaris,shakari,solaris,innocence]
