# definitions used

# constants
DE = 'DE'

# variables
qhLen = None  # number of rows of the quarter of an hour output vector (4 each hour)

header = None
zones = None
dataImport = None
dataExport = None
sumImport = None
sumExport = None
data = None


# output file names
output_file_name = 'GenerationAndLoad.csv'


# countries in the CWE area
countries_dict = {
    'AT': ['DE'],
    'BE': ['FR', 'NL'],
    'FR': ['BE', 'DE'],
    'DE': ['AT', 'FR', 'NL'],
    'NL': ['BE', 'DE']
}

PSRTYPE_MAPPINGS = {
    'A03': 'Mixed',
    'A04': 'Generation',
    'A05': 'Load',
    'B01': 'Biomass',
    'B02': 'Fossil Brown coal/Lignite',
    'B03': 'Fossil Coal-derived gas',
    'B04': 'Fossil Gas',
    'B05': 'Fossil Hard coal',
    'B06': 'Fossil Oil',
    'B07': 'Fossil Oil shale',
    'B08': 'Fossil Peat',
    'B09': 'Geothermal',
    'B10': 'Hydro Pumped Storage',
    'B11': 'Hydro Run-of-river and poundage',
    'B12': 'Hydro Water Reservoir',
    'B13': 'Marine',
    'B14': 'Nuclear',
    'B15': 'Other renewable',
    'B16': 'Solar',
    'B17': 'Waste',
    'B18': 'Wind Offshore',
    'B19': 'Wind Onshore',
    'B20': 'Other',
    'B21': 'AC Link',
    'B22': 'DC Link',
    'B23': 'Substation',
    'B24': 'Transformer'
    }
# countries_dict = {
#     #'AL': ['GR', 'ME', 'RS'],
#     'AT': ['CZ', 'DE', 'HU', 'IT', 'SI', 'CH'],
#     #'BY': ['LT', 'UA'],
#     'BE': ['FR', 'LU', 'NL'],
#     #'BA': ['HR', 'ME', 'RS'],
#     'BG': ['GR', 'MK', 'RO', 'RS', 'TR'],
#     #'HR': ['BA', 'HU', 'RS', 'SI'],
#     'CZ': ['AT', 'DE', 'PL', 'SK'],
#     'DK': ['DE', 'NO', 'SE'],
#     'EE': ['FI', 'LV', 'RU'],
#     #'MK': ['BG', 'GR', 'RS'],
#     'FI': ['EE', 'NO', 'RU', 'SE'],
#     'FR': ['BE', 'DE', 'IT', 'ES', 'CH'],
#     'DE': ['AT', 'CH', 'CZ', 'DK', 'FR', 'NL', 'PL', 'SE'],
#     'GR': ['AL', 'BG', 'IT', 'MK', 'TR'],
#     'HU': ['AT', 'HR', 'RO', 'RS', 'SK', 'UA'],
#     'IT': ['AT', 'FR', 'GR', 'MT', 'SI', 'CH'],
#     'LV': ['EE', 'LT', 'RU'],
#     'LT': ['BY', 'LV', 'PL', 'RU', 'SE'],
#     #'MT': ['IT'],
#     #'MD': ['UA'],
#     'ME': ['AL', 'BA', 'RS'],
#     'NL': ['BE', 'DE', 'NO'],
#     'NO': ['DK', 'FI', 'NL', 'SE'],
#     'PL': ['CZ', 'DE', 'LT', 'SK', 'SE', 'UA'],
#     'PT': ['ES'],
#     'RO': ['BG', 'HU', 'RS', 'UA'],
#     #'RU': ['EE', 'FI', 'LV', 'LT', 'UA'],
#     #'RS': ['AL', 'BA', 'BG', 'HR', 'HU', 'MK', 'ME', 'RO'],
#     'SK': ['CZ', 'HU', 'PL', 'UA'],
#     'SI': ['AT', 'HR', 'IT'],
#     'ES': ['FR', 'PT'],
#     'SE': ['DK', 'FI', 'DE', 'LT', 'NO', 'PL'],
#     'CH': ['AT', 'FR', 'DE', 'IT']
#     #'TR': ['BG', 'GR'],
#     #'UA': ['BY', 'HU', 'MD', 'PL', 'RO', 'RU', 'SK']
# }
