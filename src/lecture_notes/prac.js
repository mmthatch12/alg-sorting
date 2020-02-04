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