// bubble-Sort in JavaScript

function bubbleSort(ar) {
    let temp;
    for (let i = 0; i < ar.length-1; i++) {
        for (let j = 0; j < ar.length-i-1; j++) {
            if (ar[j]>ar[j+1]) {
                // [ar[j],ar[j+1]]=[ar[j+1],ar[j]]  -->can use this swapping technique as well
                temp=ar[j] ;
                ar[j]=ar[j+1];
                ar[j+1]=temp

            }            
        }
        
    }
    return ar;
}
arr=[5,4,3,2,1];
console.log("array before sorting:",arr)
swapped_array=bubbleSort(arr);
console.log("array before sorting:",swapped_array);