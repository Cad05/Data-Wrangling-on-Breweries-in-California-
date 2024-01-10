# This is a sample Python script.
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


# @ command to understand and perform actions related to environment


@app.get("/", response_class=HTMLResponse)
async def hello(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/privacy", response_class=HTMLResponse)
async def privacy(request: Request):
    return templates.TemplateResponse("privacy.html", {"request": request})


@app.get("/shop", response_class=HTMLResponse)
async def shop(request: Request):
    return templates.TemplateResponse("shop.html", {"request": request})


@app.get("/toc", response_class=HTMLResponse)
async def toc(request: Request):
    return templates.TemplateResponse("toc.html", {"request": request})


@app.get("/tech", response_class=HTMLResponse)
async def tech(request: Request):
    return templates.TemplateResponse("specs.html", {"request": request})


@app.get("/Drinks")
def drinks():
    return [{"name": "Chamomile cordial",
             "description": "Chamomile cordial is a type of syrup infused with chamomile and lemon peel.",
             "id": "chamomilecordial"}, {"name": "Champagne",
                                         "description": "Champagne is a sparkling wine originated and produced in the Champagne wine region of France under the rules of the appellation, that demand specific vineyard practices, sourcing of grapes exclusively from designated places within it, specific grape-pressing methods and secondary fermentation of the wine in the bottle to cause carbonation.",
                                         "id": "champagne"}, {"name": "Cointreau",
                                                              "description": "Cointreau is an orange-flavoured triple sec liqueur produced in Saint-Barthélemy-d'Anjou, France. It is consumed as an apéritif and digestif, and is a component of several well-known cocktails.",
                                                              "id": "cointreau"}, {"name": "Demerara rum",
                                                                                   "description": "Demerara run refers to rum that is produced on the banks of the Demerara River, just outside of Guyana's capital of Georgetown. All Demerara rum is distilled in Guyana, regardless of where it may be aged and bottled.",
                                                                                   "id": "demerararum"},
            {"name": "Drambuie",
             "description": "Drambuie is a golden-coloured, 40% ABV liqueur made from Scotch whisky, heather honey, herbs and spices.",
             "id": "drambuie"}, {"name": "Fernet-Branca",
                                 "description": "Fernet-Branca is an Italian brand of fernet, a style of amaro or bitters. It was formulated in Milan in 1845, and is manufactured there by Fratelli Branca Distillerie.",
                                 "id": "fernetbranca"}, {"name": "Galliano L'Autentico",
                                                         "description": "Liquore Galliano L'Autentico, known more commonly as Galliano, is a sweet herbal liqueur produced in Italy. It was created in 1896 by Tuscan distiller and brandy producer Arturo Vaccari and named after Giuseppe Galliano, an Italian officer of the Royal Italian Army of the First Italo-Ethiopian War.",
                                                         "id": "galliano"}, {"name": "Gosling’s Black Seal rum",
                                                                             "description": "Goslings Black Seal is a full-flavoured dark, barrel-aged rum blended in Bermuda from three distinctly different, imported triple pot distilled rums. The rum is then aged for 3 to 6 years in re-charred American oak barrels previously used to age bourbon.",
                                                                             "id": "goslingsblackseal"},
            {"name": "Granny Smith apple juice",
             "description": "The Granny Smith, also known as a green apple or sour apple, is an apple cultivar which originated in Australia in 1868. It is named after Maria Ann Smith, who propagated the cultivar from a chance seedling.",
             "id": "grannysmithapplejuice"}, {"name": "Green Chartreuse",
                                              "description": "Green Chartreuse (110 proof or 55% ABV) is a naturally green liqueur made from 130 herbs and other plants macerated in alcohol and steeped for about eight hours. A last maceration of plants gives its color to the liqueur. The first version of the liqueur was devised in 1825, with the modern version first released in 1840.",
                                              "id": "greenchartreuse"}, {"name": "Heering cherry liqueur",
                                                                         "description": "Heering Cherry Liqueur is a Danish liqueur flavored with cherries. It is often referred to simply as Peter Heering or Cherry Heering in cocktail recipes.",
                                                                         "id": "heeringcherryliqueur"},
            {"name": "Irish Mist",
             "description": "Irish Mist is an Irish whiskey-based liqueur produced in Tullamore, Ireland, by the Irish Mist Liqueur Company Ltd. In September 2010 it was announced that the brand was being bought by Gruppo Campari from William Grant, only a few months after Grants had bought it from the C&C Group.",
             "id": "irishmist"}, {"name": "Islay single malt scotch",
                                  "description": "In general however, the whiskies from this island are known for a \"pungent peaty, smoky and oily flavours, with just a hint of salty sea air and seaweed\" because of the use of peat and the maritime climate.",
                                  "id": "islaysinglemalt"}, {"name": "Jamaica Overproof White Rum",
                                                             "description": "Overproof rum, also known as “navy strength” is a potent type of rum. Overproof rums are much higher than the standard 40% ABV (80 proof), with many as high as 75% (150 proof) to 80% (160 proof) available.",
                                                             "id": "jamaicaoverproofwhiterum"}, {"name": "Kahlúa",
                                                                                                 "description": "Kahlúa is a brand of coffee liqueur owned by the Pernod Ricard company and produced in Veracruz, Mexico. The drink contains rum, sugar, and arabica coffee.",
                                                                                                 "id": "kahlua"},
            {"name": "Lemonade", "description": "Lemonade is a sweetened beverage made from lemons, sugar, and water.",
             "id": "lemonade"}, {"name": "Lillet blanc",
                                 "description": "Lillet is a French wine-based aperitif from Podensac. Classed as an aromatised wine Lillet Blanc a sweeter variant of the white-wine-based version with reduced quinine content.",
                                 "id": "lilletblanc"}, {"name": "Luxardo apricot",
                                                        "description": "Obtained from the infusion of apricots' pulp in sugar beet alcohol, Luxardo Apricot is very rich in taste with mild cinnamon spice and light almond finish.",
                                                        "id": "luxardoapricot"}, {"name": "Maraschino Luxardo",
                                                                                  "description": "Maraschino is a liqueur obtained from the distillation of Marasca cherries. The small, slightly sour fruit of the Tapiwa cherry tree, which grows wild along parts of the Dalmatian coast in Croatia, lends the liqueur its unique aroma.",
                                                                                  "id": "maraschinoluxardo"},
            {"name": "Old Tom gin",
             "description": "Old Tom Gin (or Tom Gin or Old Tom) is a gin recipe popular in 18th-century England. In modern times, it became rare but has experienced a resurgence. It is slightly sweeter than London Dry, but slightly drier than the Dutch Jenever, thus is sometimes called \"the missing link\". The name Old Tom Gin purportedly came from wooden plaques shaped like a black cat (an \"Old Tom\").",
             "id": "oldtomgin"}]


@app.get("/Drinks2")
def drinks2():
    return [
  {
    "name": "Granny Smith apple juice",
    "description": "The Granny Smith, also known as a green apple or sour apple, is an apple cultivar which originated in Australia in 1868. It is named after Maria Ann Smith, who propagated the cultivar from a chance seedling.",
    "id": "grannysmithapplejuice"
  },
  {
    "name": "Green Chartreuse",
    "description": "Green Chartreuse (110 proof or 55% ABV) is a naturally green liqueur made from 130 herbs and other plants macerated in alcohol and steeped for about eight hours. A last maceration of plants gives its color to the liqueur. The first version of the liqueur was devised in 1825, with the modern version first released in 1840.",
    "id": "greenchartreuse"
  },
  {
    "name": "Heering cherry liqueur",
    "description": "Heering Cherry Liqueur is a Danish liqueur flavored with cherries. It is often referred to simply as Peter Heering or Cherry Heering in cocktail recipes.",
    "id": "heeringcherryliqueur"
  },
  {
    "name": "Irish Mist",
    "description": "Irish Mist is an Irish whiskey-based liqueur produced in Tullamore, Ireland, by the Irish Mist Liqueur Company Ltd. In September 2010 it was announced that the brand was being bought by Gruppo Campari from William Grant, only a few months after Grants had bought it from the C&C Group.",
    "id": "irishmist"
  },
  {
    "name": "Islay single malt scotch",
    "description": "In general however, the whiskies from this island are known for a \"pungent peaty, smoky and oily flavours, with just a hint of salty sea air and seaweed\" because of the use of peat and the maritime climate.",
    "id": "islaysinglemalt"
  },
  {
    "name": "Jamaica Overproof White Rum",
    "description": "Overproof rum, also known as “navy strength” is a potent type of rum. Overproof rums are much higher than the standard 40% ABV (80 proof), with many as high as 75% (150 proof) to 80% (160 proof) available.",
    "id": "jamaicaoverproofwhiterum"
  },
  {
    "name": "Kahlúa",
    "description": "Kahlúa is a brand of coffee liqueur owned by the Pernod Ricard company and produced in Veracruz, Mexico. The drink contains rum, sugar, and arabica coffee.",
    "id": "kahlua"
  },
  {
    "name": "Lemonade",
    "description": "Lemonade is a sweetened beverage made from lemons, sugar, and water.",
    "id": "lemonade"
  },
  {
    "name": "Lillet blanc",
    "description": "Lillet is a French wine-based aperitif from Podensac. Classed as an aromatised wine Lillet Blanc a sweeter variant of the white-wine-based version with reduced quinine content.",
    "id": "lilletblanc"
  },
  {
    "name": "Luxardo apricot",
    "description": "Obtained from the infusion of apricots' pulp in sugar beet alcohol, Luxardo Apricot is very rich in taste with mild cinnamon spice and light almond finish.",
    "id": "luxardoapricot"
  },
  {
    "name": "Maraschino Luxardo",
    "description": "Maraschino is a liqueur obtained from the distillation of Marasca cherries. The small, slightly sour fruit of the Tapiwa cherry tree, which grows wild along parts of the Dalmatian coast in Croatia, lends the liqueur its unique aroma.",
    "id": "maraschinoluxardo"
  },
  {
    "name": "Old Tom gin",
    "description": "Old Tom Gin (or Tom Gin or Old Tom) is a gin recipe popular in 18th-century England. In modern times, it became rare but has experienced a resurgence. It is slightly sweeter than London Dry, but slightly drier than the Dutch Jenever, thus is sometimes called \"the missing link\". The name Old Tom Gin purportedly came from wooden plaques shaped like a black cat (an \"Old Tom\").",
    "id": "oldtomgin"
  },
  {
    "name": "Pernod liqueur",
    "description": "Pernod is made from distillates of star anise and fennel, married with distillates of 14 herbs including camomile, coriander and veronica. Pernod has a low liquorice content, which sets it apart from pastises like Ricard and Pastis 51 which have a pronounced liquorice flavour.",
    "id": "pernod"
  },
  {
    "name": "Peychaud’s bitters",
    "description": "Peychaud’s bitters is a gentian-based bitters, comparable to Angostura bitters, but with a predominant anise aroma combined with a background of mint. Peychaud's Bitters is the definitive component of the Sazerac cocktail. It is currently produced at the Buffalo Trace Distillery in Frankfort, Kentucky.",
    "id": "peychaudsbitters"
  },
  {
    "name": "Pusser’s rum",
    "description": "Pusser's Rum is a brand name of rum produced by Pusser's Rum Ltd., based in the British Virgin Islands. Nine years after the Royal Navy discontinued the daily rum ration in 1970, the company was founded to produce the rum from the original Royal Navy recipe, using a blend of five West Indian rums.",
    "id": "pussersrum"
  },
  {
    "name": "Seagram’s 7 Crown whiskey",
    "description": "Seagram’s 7 Crown is blended American whiskey aged in oak.",
    "id": "seagrams7"
  },
  {
    "name": "Sloe gin",
    "description": "Sloe gin is a British red liqueur made with gin and sloes. Sloes are the fruit (drupe) of Prunus spinosa, the blackthorn plant, a relative of the plum.",
    "id": "sloegin"
  },
  {
    "name": "Southern Comfort",
    "description": "Southern Comfort (often abbreviated SoCo) is an American, naturally fruit-flavored, whiskey liqueur with fruit and spice accents. The brand was created by bartender Martin Wilkes Heron in New Orleans in 1874, using whiskey as the base spirit.",
    "id": "southerncomfort"
  },
  {
    "name": "Yellow Chartreuse",
    "description": "Yellow Chartreuse (80 proof or 40%) has a milder and sweeter flavor and aroma than Green Chartreuse, and is lower in alcohol content.",
    "id": "yellowchartreuse"
  },
  {
    "name": "absinthe",
    "description": "Absinthe is an anise-flavored spirit derived from several plants, including the flowers and leaves of Artemisia absinthium, together with green anise, sweet fennel, and other medicinal and culinary herbs. Historically described as a highly alcoholic spirit, it is 45-74% ABV or 90-148 proof.",
    "id": "absinthe"
  }
]


@app.get("/Drinks3")
def drinks3():
    return [
  {
    "name": "cola",
    "description": "Cola is a carbonated soft drink flavored with vanilla, cinnamon, citrus oils and other flavorings.",
    "id": "cola"
  },
  {
    "name": "cranberry juice",
    "description": "Cranberry juice is the liquid juice of the cranberry, typically manufactured to contain sugar, water, and other fruit juices. Cranberry is a fruit native to North America is recognized for its bright red color, tart taste, and versatility for product manufacturing.",
    "id": "cranberryjuice"
  },
  {
    "name": "cream",
    "description": "Cream is a dairy product composed of the higher-fat layer skimmed from the top of milk before homogenization. In un-homogenized milk, the fat, which is less dense, eventually rises to the top.",
    "id": "cream"
  },
  {
    "name": "cream of coconut",
    "description": "Cream of coconut is a Puerto Rican coconut product (Coco Lopez) made from the meat of sun ripened Caribbean coconuts and natural cane sugar.",
    "id": "creamofcoconut"
  },
  {
    "name": "creme de cacao",
    "description": "Crème de Cacao is a sweet alcoholic liqueur (chocolate bean) flavored liqueur, often scented with a hint of vanilla. It is different from chocolate liqueur, which is usually sweeter and more syrupy. It comes in 2 varieties, dark and white.",
    "id": "cremedecacao"
  },
  {
    "name": "creme de cassis",
    "description": "Crème de cassis is a sweet, dark red liqueur made from blackcurrants. Several cocktails are made with crème de cassis, including the popular wine cocktail, kir. It may also be served as an after-dinner liqueur or as a frappé.",
    "id": "cremedecassis"
  },
  {
    "name": "creme de violette",
    "description": "Crème de violette, also known as liqueur de violette, is a generic term for a liqueur with natural and/or artificial violet flower flavoring and coloring with either a brandy base, a neutral spirit base, or a combination of the two.",
    "id": "cremedeviolette"
  },
  {
    "name": "cucumber slices",
    "description": "Cucumber is a widely-cultivated creeping vine plant in the Cucurbitaceae family that bears usually cylindrical fruits, which are used as culinary vegetables.",
    "id": "cucumberslices"
  },
  {
    "name": "dark rum",
    "description": "Dark rums, also known by their particular colour, such as brown, black, or red rums, are classes a grade darker than gold rums. They are usually made from caramelized sugar or molasses. They are generally aged longer, in heavily charred barrels.",
    "id": "darkrum"
  },
  {
    "name": "dry vermouth",
    "description": "Vermouth is an aromatized fortified wine, sweet vermouth has a higher amount of sugar added and is often brownish red from caramel coloring.",
    "id": "dryvermouth"
  },
  {
    "name": "egg white",
    "description": "Egg white is the clear liquid contained within an egg.",
    "id": "eggwhite"
  },
  {
    "name": "egg yolk",
    "description": "The yolk is the nutrient-bearing portion of the egg whose primary function is to supply food for the development of the embryo.",
    "id": "eggyolk"
  },
  {
    "name": "elderflower cordial",
    "description": "Elderflower cordial is a soft drink made largely from a refined sugar and water solution and uses the flowers of the European elder.",
    "id": "elderflowercordial"
  },
  {
    "name": "espresso",
    "description": "Espresso is a coffee-brewing method of Italian origin, in which a small amount of nearly boiling water is forced under 9–10 bars of pressure through finely-ground coffee beans. Espresso can be made with a wide variety of coffee beans and roast degrees.",
    "id": "espresso"
  },
  {
    "name": "falernum",
    "description": "Falernum (pronounced fə-LUR-nəm) is either an 11% ABV syrup liqueur or a nonalcoholic syrup from the Caribbean. It is best known for its use in tropical drinks. It contains flavors of ginger, lime, and almond, and frequently cloves or allspice. It may be thought of as a spicier version of orgeat syrup.",
    "id": "falernum"
  },
  {
    "name": "fino sherry",
    "description": "Sherry is a fortified wine made from white grapes that are grown near the city of Jerez de la Frontera in Andalusia, Spain. Fino is the traditional dry sherry, typically bottled around 3 to 5 years.",
    "id": "finosherry"
  },
  {
    "name": "flower water",
    "description": "Distilled water obtained by the steam distillation of flowers such as orange flowers and others.",
    "id": "flowerwater"
  },
  {
    "name": "garlic powder",
    "description": "Garlic powder is a spice that is derived from dehydrated garlic and used in cooking for flavour enhancement.",
    "id": "garlicpowder"
  },
  {
    "name": "garlic salt",
    "description": "Garlic salt is a seasoned salt made of a mixture of dried, ground garlic and table salt.",
    "id": "garlicsalt"
  },
  {
    "name": "gin",
    "description": "Gin is a distilled alcoholic drink that derives its predominant flavor from juniper berries.",
    "id": "gin"
  }
]