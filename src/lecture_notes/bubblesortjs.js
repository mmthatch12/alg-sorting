function bubblesort(arr){
    let finarr = [...arr]
    let sorted = true
    while(sorted){
      sorted = false
      for(let i=0;i<finarr.length-1;i++){
        if(finarr[i] > finarr[i+1]){
          let val1 = finarr[i]
          let val2 = finarr[i+1]
          finarr[i] = val2
          finarr[i+1] = val1
          sorted = true
        }
      }
    }
    return finarr
  }
  console.log(bubblesort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))