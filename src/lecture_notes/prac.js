function threeNumberSum(arr, target) {
    let finarr = []
    let firarr = arr.sort((a,b) => a-b)
    return firarr
    for(let i = 0;i<firarr.length;i++){
      for(let j=1;j<firarr.length-1;j++){
        console.log("outside:", firarr[i], firarr[j], firarr[j+1])
        if(firarr[i]+firarr[j]+firarr[j+1] == target && firarr[i] !== firarr[j] && firarr[i] !== firarr[j+1]){
          console.log("outside:", firarr[i], firarr[j], firarr[j+1])
          finarr.push([firarr[i], firarr[j], firarr[j+1]])
        }
      }
    }
    for(let i = 0;i<finarr.length;i++){
      finarr[i].sort((a,b) => a-b) 
    }
    return finarr

    
}
console.log(threeNumberSum([12,3,1,2,-6,5,0,-8,-1,6,-5], 0))

function getEquivalent(note) {
	let nob = {'C#': 'Db', 'D#': 'Eb', 'F#': 'Gb', 'G#': 'Ab', 'A#': 'Bb', 'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#', 'Bb': 'A#'}

  for(let item in nob){
    if(nob[item] == note){
      return item
    }
  }
}

console.log(getEquivalent('Db'))

function hasValidPrice(product) {
	
	if(product){
		let holder = product.price
		if(typeof holder == 'number'){
			if(product.price >= 0){
				return true
			}else{
				return false
			}
		}else{
			return false
		}
	} else{
		return false
	}
  
}

Test.assertEquals(hasValidPrice({ "product": "Milk", price: 1.50 }), true)
Test.assertEquals(hasValidPrice({ "product": "Cheese", price: -1 }), false)
Test.assertEquals(hasValidPrice({ "product": "Eggs", price: 0 }), true)
Test.assertEquals(hasValidPrice({ "product": "Flour" }), false)
Test.assertEquals(hasValidPrice({ "product": "Cerials", price: '3.0' }), false)
Test.assertEquals(hasValidPrice({ "product": "Beer", price: NaN }), false)
Test.assertEquals(hasValidPrice(), false)

function capLast(txt) {
	let splity = txt.split(' ')
  let nespl = []
  let ite = null
  let oth = ''
  for(let i=0;i<splity.length;i++){
    ite = splity[i].split('')
    ite[ite.length-1] = ite[ite.length-1].toUpperCase()
    console.log(ite)
    oth = ite.join("")
    nespl.push(oth)
    console.log(oth)
  }
  return nespl.join(' ')

}
console.log(capLast("My Name Is Edabit"))

function clearFog(str) {
	let splity = str.split('')
	let filted = splity.filter(item => item !== "f" && item !== "o" && item !== "g")
  let last = filted.join('')
  if(last.length == str.length){
    return "It's a clear day!"
  }else{
  return last
  }
}
console.log(clearFog("fogfogfffoooofftreesggfoogfog"))

function findLargestNums(arr) {
	let finarr = []
  for(let i = 0;i<arr.length;i++){
    finarr.push(Math.max(...arr[i]))
  }
  return finarr
}
console.log(findLargestNums([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]))


function indexMultiplier(arr) {
	let mapy = arr.map((num, ind) => num*ind)
	let rudy = mapy.reduce((cur,acc) => cur+acc)
	if(arr.length == 0){
		return 0
	} else {
		return rudy
	}
}
console.log(indexMultiplier([-3, 0, 8, -6]))

function convert(hours, minutes) {
	return (hours*60)*60 + (minutes*60)
}