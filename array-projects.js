var score = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54];
var solution1 = score [0];
var solution2 = score [1];
var solution3 = score [2];
var solution4 = score [3];
alert("Solution 3 produced " + solution3 + " bubbles!");

var flavors = ["cannabis", "Chunky Monkey", " chocolate", " French Vanilla", "Rum Raisin" ];
flavors[0]= "Vanilla ChocoChip";

var products = ["hadlebars", "mobile phones", "pens", "pencils" ];
var lastProductmade = products.length-1;
var recentproductmade= products[lastProductmade];
  

function makeAPhrase (){
 var word1 = ["Waz Up", "Sucky Sucky", "Chopy Chopy", "Vada Ving", "Vada Vunm"]
 var word2 = ["Trumper", "Out there!", "MOSt folf", "Wolf of Wall Street", "lambo" ];
  var word3 = [ "Porche", "Samsung", "Motorola", "Wolfagangpck", " DOODOO DID"];
  
  var rand1 = Math.floor (Math.random() * word1.length);
  var rand2 = Math.floor (Math.random() * word2.length);
  var rand3 = Math.floor (Math.random() * word3.length);
  
  var phraseOfTheDay = word1[rand1] + " " + word2[rand2] + " " + word3[rand3];
  
  alert(phraseOfTheDay);
  console.log(phraseOfTheDay)
}
makeAPhrase();

var scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]; 
var outPut; 
var index = 0;
while (index < scores.length) 
{ 
  outPut = "Bubble Solution  # " + index + " Score : " + scores [index]; console.log(outPut); index = index + 1;
}
