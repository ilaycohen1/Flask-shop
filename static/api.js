const API_URL="https://catfact.ninja/fact";
const Bitcoin_URL="https://api.coindesk.com/v1/bpi/currentprice.json";


function getCat(){
    axios.get(API_URL).then((response)=>{
        document.getElementById("fact").innerHTML=response.data.fact;
    }
    )
}

function getBitRate(){
    axios.get(Bitcoin_URL).then((response)=>{
        document.getElementById("main").innerHTML=response.data.bpi.USD.rate;
    }
    )
}

function getBitCode(){
    axios.get(Bitcoin_URL).then((response)=>{
        document.getElementById("main").innerHTML=response.data.bpi.USD.code;
    }
    )
}
    

document.getElementById("changeButton").addEventListener("click", ()=>getCat());
document.getElementById("changeButton2").addEventListener("click", ()=>getBitCode());
document.getElementById("changeButton3").addEventListener("click", ()=>getBitRate());


getCat();


