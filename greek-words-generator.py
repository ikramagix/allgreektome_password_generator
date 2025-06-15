# greek-generator.py

import random

# fake but Greek-sounding morpheme parts
roots = [
    "crypto", "philo", "gastro", "morpho", "lepto", "thermo", "therma", "thermi",
    "neuro", "psycho", "karyo", "soma", "chrono", "dromo", "xeno", "cyto", "rhino",
    "photo", "auto", "meta", "gnoso", "pneumo", "hemo", "derma", "sphero", "klepto",
    "tropo", "nomo", "anthropo", "astro", "bio", "cyclo", "dyna", "ethno", "geo",
    "heli", "hydro", "iso", "mega", "micro", "mono", "neo", "orpho", "ortho",
    "phon", "poly", "pseudo", "zo", "acro", "agogo", "agon", "aero", "agri", "algo",
    "ambi", "amphi", "ana", "baro", "biblio", "blasto", "cardio", "cata", "centro",
    "chiro", "chromo", "cosmo", "crano", "cyano", "dento", "dermato", "dys", "echo",
    "ecto", "endo", "epi", "ergo", "esthesio", "gamo", "glosso", "glyco", "hemi",
    "hetero", "homo", "hyper", "hypo", "ichthyo", "idio", "leuko", "lycano", "miso",
    "nauto", "necro", "odonto", "palaeo", "pan", "patho", "pedo", "peri", "phago",
    "phreno", "plasto", "podo", "scopo", "seismo", "sopho", "tachy", "tecto",
    "tele", "theo", "toxo"
]

connectors = ["o", "i", "y", ""]  # mimics linker

suffixes = [
    "logy", "phobia", "pathia", "cratia", "morphosis", "genesis", "tropikon",
    "phoros", "nomikon", "plastikon", "grammateia", "dynamikon", "gnomonikon",
    "meter", "scope", "graph", "nomy", "phile", "mania", "lysis", "oid", "techne",
    "phagy", "pathy", "phasia", "trophy", "osis", "itis", "agogue", "archy",
    "cracy", "crat", "poly", "ergy", "gamous", "log", "nym", "gram", "phone",
    "phonic", "naut", "sophy", "matic", "etic", "blast", "cephaly", "coccus",
    "centesis", "cide", "derma", "dipsia", "ectomy", "emia", "genic", "genous",
    "gon", "hedron", "iatric", "iasis", "ist", "kinesis", "lalia", "latry",
    "machy", "mancy", "megaly", "mere", "morph", "nomics", "nomic", "oma",
    "onym", "phage", "phany", "philia", "plegia", "pnea", "pod", "poeia", "pter",
    "ptosis", "rrhage", "rrhagia", "rrhaphy", "rrhea", "saur", "stasis", "stome",
    "strophy", "tectic", "thermic", "tome", "tomy", "topia", "tropic", "urgy",
    "zyme", "otic"
]

def generate_fake_greek_word():
    parts = [random.choice(roots)]
    for _ in range(random.randint(2, 4)):
        parts.append(random.choice(connectors))
        parts.append(random.choice(roots))
    word = ''.join(parts) + random.choice(connectors) + random.choice(suffixes)
    return word

# Generate 500 unique fake words
fake_words = set()
while len(fake_words) < 500:
    fake_words.add(generate_fake_greek_word())

# Write to words.ts in TypeScript format
with open("words.ts", "w", encoding="utf-8") as f:
    f.write("export const wordList = [\n")
    for w in sorted(fake_words):
        f.write(f"  '{w}',\n")
    f.write("];\n")

print("populated words.ts with 500 fake long Greek words")
