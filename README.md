# Final Api Docs

### Evenementenkalender Limburg - Eindproject API Development

##### Kuno Claes - R0937868

##### Beschrijving thema

Voor mijn eindproject van API Development koos ik als thema een evenementenkalender in Limburg.

De data van de verschillende evenementen die ik bijhoud zijn:

- Naam
- Stad
- Begindatum
- Einddatum
- Betalend?

#### Gemaakte deelopdrachten

- Algemene eisen (50%)
- Aanvullende functies: 
    - Test alle niet-GET eindpoints
    - Testfile wordt gerund door Github actions
    - Een front-end die alle GET en POST endpoints bevat
    - Front-end gehost op netlify

De geschatte eindscore ligt rond de 85%

#### Hostomgeving

Mijn API wordt gehost op [OktetoCloud](https://event-api-service-icodesdeveloper.cloud.okteto.net)
Ook is er een front-end op [Netlify](https://6594876c4383a51b3b56deea--admirable-strudel-1e638c.netlify.app)

#### Werking van de API

- GET, /events/: Laat alle evenementen zien   
    [![image.png](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apiw1.png)](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apiw1.png)
- GET, /events/id/{id}: Laat een specifieke evenement zien  
    [![image.png](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apiw2.png)](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apiw2.png)
- GET, /events/city/{City}: Laat evenementen in een specifieke stad zien  
    [![image.png](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apiw3.png)](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apiw3.png)
- POST, /events/: Maak een evenement aan  
    [![image.png](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apiw4.png)](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apiw4.png)
- PUT, /events/id/{id}: Update een volledig evenement  
    [![image.png](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apiw5.png)](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apiw5.png)
- DELETE, /events/{id}: Verwijder een evenement  
    [![image.png](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apiw6.png)](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apiw6.png)
- POST, /users/: Maak een nieuwe gebruiker aan  
    [![image.png](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apiw7.png)](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apiw7.png)

#### OpenAPI Documentatie

[![image.png](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid1.png)](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid1.png)

[![image.png](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid2.png)](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid2.png)

[![image.png](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid3.png)](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid3.png)

[![image.png](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid4.png)](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid4.png)

[![image.png](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid5.png)](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid5.png)

[![image.png](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid6.png)](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid6.png)

[![image.png](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid7.png)](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid7.png)

[![image.png](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid8.png)](https://raw.githubusercontent.com/icodesdeveloper/API-FINAL/main/assets/images/apid8.png)


#### Github Actions PyTest:

[![image.png](https://github.com/icodesdeveloper/API-FINAL/blob/main/assets/images/pyt1.png?raw=true)](https://github.com/icodesdeveloper/API-FINAL/blob/main/assets/images/pyt1.png?raw=true)

#### Werkende front-end op netlify
[![image.png](https://github.com/icodesdeveloper/API-FINAL/blob/main/assets/images/apif1.png?raw=true)](https://github.com/icodesdeveloper/API-FINAL/blob/main/assets/images/apif1.png?raw=true)

[![image.png](https://github.com/icodesdeveloper/API-FINAL/blob/main/assets/images/apif2.png?raw=true)](https://github.com/icodesdeveloper/API-FINAL/blob/main/assets/images/apif2.png?raw=true)

[![image.png](https://github.com/icodesdeveloper/API-FINAL/blob/main/assets/images/apif3.png?raw=true)](https://github.com/icodesdeveloper/API-FINAL/blob/main/assets/images/apif3.png?raw=true)

[![image.png](https://github.com/icodesdeveloper/API-FINAL/blob/main/assets/images/apif4.png?raw=true)](https://github.com/icodesdeveloper/API-FINAL/blob/main/assets/images/apif4.png?raw=true)