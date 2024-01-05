<h1>FOOTBALL DATA API - WEB SCRAPPING PROJECT</h1>
<p>This is a webscrapping tool created with Python DJANGO</p></br>
<i>NOTE that this is only an API, only POST requests in BODY should be made to this -> https://skore.vercel.app </i>
![reac](https://github.com/JeremiahJacob261/skore/assets/69473368/7a132ea7-acb6-4605-a572-fc73d8a22274)
<img src='https://github-production-user-asset-6210df.s3.amazonaws.com/69473368/294429914-7a132ea7-acb6-4605-a572-fc73d8a22274.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240105%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240105T080740Z&X-Amz-Expires=300&X-Amz-Signature=b9ab8bac63bd6a5e1c9aad2880191f86be0103a888384672451e12f35a465f8a&X-Amz-SignedHeaders=host&actor_id=69473368&key_id=0&repo_id=736969114'/>
The Image link above is an example of how an API request should be made using THUNDERCLIENT[ https://www.thunderclient.com/ ]
    
```js
//this is an exampke of how to fetch the data using JAVASCRIPT
try {
                            let test = await fetch('https://skore.vercel.app', {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json'
                                },
                                body: JSON.stringify({"day":0})
                            }).then(data => {
                                return data.json();
                            })
                           console.log(test)
                        } catch (error) {
                            console.log(error)
                        }

```
<p># {"day":0} , the value 0 is the distance from today, -1, -2 for previous days, 1, 2 for subsequent days</p></br>


<sub>DATA is scrapped from flashscore.mobi and API hosted on vercel</sub>

