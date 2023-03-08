# About
A forecasting package for World Bank indicators. Here are a couple figures generated with the corresponding command.  

If you are not sure, run generate.sh for a randomly generated command: ```bash generate.sh``` 

# API
https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information

# Examples
```python main.py usa chn rus gdp internet electricity```

![1](https://github.com/markdoughten/worldbank/blob/documentation/docs/images/Figure_1.png)

```python main.py can mex usa population export import```

![2](https://github.com/markdoughten/worldbank/blob/documentation/docs/images/Figure_1.png)

# Commands
```python main.py help```

| command      | description                   | syntax                      | units   |
|:-------------|:------------------------------|:----------------------------|:--------|
| countries    | country codes                 | countries <letter>          |         |
| electricity  | electricity access            | electricity <country_code>  | %       |
| export       | goods and services exported   | export <country_code>       | $       |
| gdp          | gross domestic product        | gdp <country_code>          | $       |
| help         | programmed commands           | help <command>              |         |
| import       | goods and services imported   | import <country_code>       | $       |
| internet     | broadband subscriptions       | internet <country_code>     |         |
| land         | land for agriculture          | land <country code>         | %       |
| population   | population size               | population <country code>   |         |
| unemployment | unemployed seeking employment | unemployment <country_code> | %       |

# Countries
```python main.py countries```

| code   | country                                                                          |
|:-------|:---------------------------------------------------------------------------------|
| abw    | Aruba                                                                            |
| afe    | Africa Eastern and Southern                                                      |
| afg    | Afghanistan                                                                      |
| afr    | Africa                                                                           |
| afw    | Africa Western and Central                                                       |
| ago    | Angola                                                                           |
| alb    | Albania                                                                          |
| and    | Andorra                                                                          |
| arb    | Arab World                                                                       |
| are    | United Arab Emirates                                                             |
| arg    | Argentina                                                                        |
| arm    | Armenia                                                                          |
| asm    | American Samoa                                                                   |
| atg    | Antigua and Barbuda                                                              |
| aus    | Australia                                                                        |
| aut    | Austria                                                                          |
| aze    | Azerbaijan                                                                       |
| bdi    | Burundi                                                                          |
| bea    | East Asia & Pacific (IBRD-only countries)                                        |
| bec    | Europe & Central Asia (IBRD-only countries)                                      |
| bel    | Belgium                                                                          |
| ben    | Benin                                                                            |
| bfa    | Burkina Faso                                                                     |
| bgd    | Bangladesh                                                                       |
| bgr    | Bulgaria                                                                         |
| bhi    | IBRD countries classified as high income                                         |
| bhr    | Bahrain                                                                          |
| bhs    | Bahamas, The                                                                     |
| bih    | Bosnia and Herzegovina                                                           |
| bla    | Latin America & the Caribbean (IBRD-only countries)                              |
| blr    | Belarus                                                                          |
| blz    | Belize                                                                           |
| bmn    | Middle East & North Africa (IBRD-only countries)                                 |
| bmu    | Bermuda                                                                          |
| bol    | Bolivia                                                                          |
| bra    | Brazil                                                                           |
| brb    | Barbados                                                                         |
| brn    | Brunei Darussalam                                                                |
| bss    | Sub-Saharan Africa (IBRD-only countries)                                         |
| btn    | Bhutan                                                                           |
| bwa    | Botswana                                                                         |
| caa    | Sub-Saharan Africa (IFC classification)                                          |
| caf    | Central African Republic                                                         |
| can    | Canada                                                                           |
| cea    | East Asia and the Pacific (IFC classification)                                   |
| ceb    | Central Europe and the Baltics                                                   |
| ceu    | Europe and Central Asia (IFC classification)                                     |
| che    | Switzerland                                                                      |
| chi    | Channel Islands                                                                  |
| chl    | Chile                                                                            |
| chn    | China                                                                            |
| civ    | Cote d'Ivoire                                                                    |
| cla    | Latin America and the Caribbean (IFC classification)                             |
| cme    | Middle East and North Africa (IFC classification)                                |
| cmr    | Cameroon                                                                         |
| cod    | Congo, Dem. Rep.                                                                 |
| cog    | Congo, Rep.                                                                      |
| col    | Colombia                                                                         |
| com    | Comoros                                                                          |
| cpv    | Cabo Verde                                                                       |
| cri    | Costa Rica                                                                       |
| csa    | South Asia (IFC classification)                                                  |
| css    | Caribbean small states                                                           |
| cub    | Cuba                                                                             |
| cuw    | Curacao                                                                          |
| cym    | Cayman Islands                                                                   |
| cyp    | Cyprus                                                                           |
| cze    | Czechia                                                                          |
| dea    | East Asia & Pacific (IDA-eligible countries)                                     |
| dec    | Europe & Central Asia (IDA-eligible countries)                                   |
| deu    | Germany                                                                          |
| dfs    | IDA countries classified as Fragile Situations                                   |
| dji    | Djibouti                                                                         |
| dla    | Latin America & the Caribbean (IDA-eligible countries)                           |
| dma    | Dominica                                                                         |
| dmn    | Middle East & North Africa (IDA-eligible countries)                              |
| dnf    | IDA countries not classified as Fragile Situations                               |
| dnk    | Denmark                                                                          |
| dns    | IDA countries in Sub-Saharan Africa not classified as fragile situations         |
| dom    | Dominican Republic                                                               |
| dsa    | South Asia (IDA-eligible countries)                                              |
| dsf    | IDA countries in Sub-Saharan Africa classified as fragile situations             |
| dss    | Sub-Saharan Africa (IDA-eligible countries)                                      |
| dza    | Algeria                                                                          |
| eap    | East Asia & Pacific (excluding high income)                                      |
| ear    | Early-demographic dividend                                                       |
| eas    | East Asia & Pacific                                                              |
| eca    | Europe & Central Asia (excluding high income)                                    |
| ecs    | Europe & Central Asia                                                            |
| ecu    | Ecuador                                                                          |
| egy    | Egypt, Arab Rep.                                                                 |
| emu    | Euro area                                                                        |
| eri    | Eritrea                                                                          |
| esp    | Spain                                                                            |
| est    | Estonia                                                                          |
| eth    | Ethiopia                                                                         |
| euu    | European Union                                                                   |
| fcs    | Fragile and conflict affected situations                                         |
| fin    | Finland                                                                          |
| fji    | Fiji                                                                             |
| fra    | France                                                                           |
| fro    | Faroe Islands                                                                    |
| fsm    | Micronesia, Fed. Sts.                                                            |
| fxs    | IDA countries classified as fragile situations, excluding Sub-Saharan Africa     |
| gab    | Gabon                                                                            |
| gbr    | United Kingdom                                                                   |
| geo    | Georgia                                                                          |
| gha    | Ghana                                                                            |
| gib    | Gibraltar                                                                        |
| gin    | Guinea                                                                           |
| gmb    | Gambia, The                                                                      |
| gnb    | Guinea-Bissau                                                                    |
| gnq    | Equatorial Guinea                                                                |
| grc    | Greece                                                                           |
| grd    | Grenada                                                                          |
| grl    | Greenland                                                                        |
| gtm    | Guatemala                                                                        |
| gum    | Guam                                                                             |
| guy    | Guyana                                                                           |
| hic    | High income                                                                      |
| hkg    | Hong Kong SAR, China                                                             |
| hnd    | Honduras                                                                         |
| hpc    | Heavily indebted poor countries (HIPC)                                           |
| hrv    | Croatia                                                                          |
| hti    | Haiti                                                                            |
| hun    | Hungary                                                                          |
| ibb    | IBRD, including blend                                                            |
| ibd    | IBRD only                                                                        |
| ibt    | IDA & IBRD total                                                                 |
| ida    | IDA total                                                                        |
| idb    | IDA blend                                                                        |
| idn    | Indonesia                                                                        |
| idx    | IDA only                                                                         |
| imn    | Isle of Man                                                                      |
| ind    | India                                                                            |
| inx    | Not classified                                                                   |
| irl    | Ireland                                                                          |
| irn    | Iran, Islamic Rep.                                                               |
| irq    | Iraq                                                                             |
| isl    | Iceland                                                                          |
| isr    | Israel                                                                           |
| ita    | Italy                                                                            |
| jam    | Jamaica                                                                          |
| jor    | Jordan                                                                           |
| jpn    | Japan                                                                            |
| kaz    | Kazakhstan                                                                       |
| ken    | Kenya                                                                            |
| kgz    | Kyrgyz Republic                                                                  |
| khm    | Cambodia                                                                         |
| kir    | Kiribati                                                                         |
| kna    | St. Kitts and Nevis                                                              |
| kor    | Korea, Rep.                                                                      |
| kwt    | Kuwait                                                                           |
| lac    | Latin America & Caribbean (excluding high income)                                |
| lao    | Lao PDR                                                                          |
| lbn    | Lebanon                                                                          |
| lbr    | Liberia                                                                          |
| lby    | Libya                                                                            |
| lca    | St. Lucia                                                                        |
| lcn    | Latin America & Caribbean                                                        |
| ldc    | Least developed countries: UN classification                                     |
| lic    | Low income                                                                       |
| lie    | Liechtenstein                                                                    |
| lka    | Sri Lanka                                                                        |
| lmc    | Lower middle income                                                              |
| lmy    | Low & middle income                                                              |
| lso    | Lesotho                                                                          |
| lte    | Late-demographic dividend                                                        |
| ltu    | Lithuania                                                                        |
| lux    | Luxembourg                                                                       |
| lva    | Latvia                                                                           |
| mac    | Macao SAR, China                                                                 |
| maf    | St. Martin (French part)                                                         |
| mar    | Morocco                                                                          |
| mco    | Monaco                                                                           |
| mda    | Moldova                                                                          |
| mde    | Middle East (developing only)                                                    |
| mdg    | Madagascar                                                                       |
| mdv    | Maldives                                                                         |
| mea    | Middle East & North Africa                                                       |
| mex    | Mexico                                                                           |
| mhl    | Marshall Islands                                                                 |
| mic    | Middle income                                                                    |
| mkd    | North Macedonia                                                                  |
| mli    | Mali                                                                             |
| mlt    | Malta                                                                            |
| mmr    | Myanmar                                                                          |
| mna    | Middle East & North Africa (excluding high income)                               |
| mne    | Montenegro                                                                       |
| mng    | Mongolia                                                                         |
| mnp    | Northern Mariana Islands                                                         |
| moz    | Mozambique                                                                       |
| mrt    | Mauritania                                                                       |
| mus    | Mauritius                                                                        |
| mwi    | Malawi                                                                           |
| mys    | Malaysia                                                                         |
| nac    | North America                                                                    |
| naf    | North Africa                                                                     |
| nam    | Namibia                                                                          |
| ncl    | New Caledonia                                                                    |
| ner    | Niger                                                                            |
| nga    | Nigeria                                                                          |
| nic    | Nicaragua                                                                        |
| nld    | Netherlands                                                                      |
| nor    | Norway                                                                           |
| npl    | Nepal                                                                            |
| nrs    | Non-resource rich Sub-Saharan Africa countries                                   |
| nru    | Nauru                                                                            |
| nxs    | IDA countries not classified as fragile situations, excluding Sub-Saharan Africa |
| nzl    | New Zealand                                                                      |
| oed    | OECD members                                                                     |
| omn    | Oman                                                                             |
| oss    | Other small states                                                               |
| pak    | Pakistan                                                                         |
| pan    | Panama                                                                           |
| per    | Peru                                                                             |
| phl    | Philippines                                                                      |
| plw    | Palau                                                                            |
| png    | Papua New Guinea                                                                 |
| pol    | Poland                                                                           |
| pre    | Pre-demographic dividend                                                         |
| pri    | Puerto Rico                                                                      |
| prk    | Korea, Dem. People's Rep.                                                        |
| prt    | Portugal                                                                         |
| pry    | Paraguay                                                                         |
| pse    | West Bank and Gaza                                                               |
| pss    | Pacific island small states                                                      |
| pst    | Post-demographic dividend                                                        |
| pyf    | French Polynesia                                                                 |
| qat    | Qatar                                                                            |
| rou    | Romania                                                                          |
| rrs    | Resource rich Sub-Saharan Africa countries                                       |
| rus    | Russian Federation                                                               |
| rwa    | Rwanda                                                                           |
| sas    | South Asia                                                                       |
| sau    | Saudi Arabia                                                                     |
| sdn    | Sudan                                                                            |
| sen    | Senegal                                                                          |
| sgp    | Singapore                                                                        |
| slb    | Solomon Islands                                                                  |
| sle    | Sierra Leone                                                                     |
| slv    | El Salvador                                                                      |
| smr    | San Marino                                                                       |
| som    | Somalia                                                                          |
| srb    | Serbia                                                                           |
| ssa    | Sub-Saharan Africa (excluding high income)                                       |
| ssd    | South Sudan                                                                      |
| ssf    | Sub-Saharan Africa                                                               |
| sst    | Small states                                                                     |
| stp    | Sao Tome and Principe                                                            |
| sur    | Suriname                                                                         |
| svk    | Slovak Republic                                                                  |
| svn    | Slovenia                                                                         |
| swe    | Sweden                                                                           |
| swz    | Eswatini                                                                         |
| sxm    | Sint Maarten (Dutch part)                                                        |
| sxz    | Sub-Saharan Africa excluding South Africa                                        |
| syc    | Seychelles                                                                       |
| syr    | Syrian Arab Republic                                                             |
| tca    | Turks and Caicos Islands                                                         |
| tcd    | Chad                                                                             |
| tea    | East Asia & Pacific (IDA & IBRD countries)                                       |
| tec    | Europe & Central Asia (IDA & IBRD countries)                                     |
| tgo    | Togo                                                                             |
| tha    | Thailand                                                                         |
| tjk    | Tajikistan                                                                       |
| tkm    | Turkmenistan                                                                     |
| tla    | Latin America & the Caribbean (IDA & IBRD countries)                             |
| tls    | Timor-Leste                                                                      |
| tmn    | Middle East & North Africa (IDA & IBRD countries)                                |
| ton    | Tonga                                                                            |
| tsa    | South Asia (IDA & IBRD)                                                          |
| tss    | Sub-Saharan Africa (IDA & IBRD countries)                                        |
| tto    | Trinidad and Tobago                                                              |
| tun    | Tunisia                                                                          |
| tur    | Turkiye                                                                          |
| tuv    | Tuvalu                                                                           |
| twn    | Taiwan, China                                                                    |
| tza    | Tanzania                                                                         |
| uga    | Uganda                                                                           |
| ukr    | Ukraine                                                                          |
| umc    | Upper middle income                                                              |
| ury    | Uruguay                                                                          |
| usa    | United States                                                                    |
| uzb    | Uzbekistan                                                                       |
| vct    | St. Vincent and the Grenadines                                                   |
| ven    | Venezuela, RB                                                                    |
| vgb    | British Virgin Islands                                                           |
| vir    | Virgin Islands (U.S.)                                                            |
| vnm    | Vietnam                                                                          |
| vut    | Vanuatu                                                                          |
| wld    | World                                                                            |
| wsm    | Samoa                                                                            |
| xkx    | Kosovo                                                                           |
| xzn    | Sub-Saharan Africa excluding South Africa and Nigeria                            |
| yem    | Yemen, Rep.                                                                      |
| zaf    | South Africa                                                                     |
| zmb    | Zambia                                                                           |
| zwe    | Zimbabwe                                                                         |



