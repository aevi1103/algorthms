let arr = [1,2,3,4,5,6,7,8,9]

const binarySearch = (arr, target) => {
    const midIndex = Math.floor(arr.length / 2)
    const mid = arr[midIndex]
    if (target === mid) return true
    if (midIndex === 0) return false

    if (target < mid) {
        temp = arr.slice(0, midIndex + 1)
        return binarySearch(temp, target)
    } else {
        temp = arr.slice(-midIndex)
        return binarySearch(temp, target)
    }
}

const start = 0
const end = arr.length - 1

const binarySearch2 = (arr, start, end, target) => {
    if (start > end) return false
    const midIndex = Math.floor((start + end) / 2)
    const mid = arr[midIndex]
    if (target === mid) return true
    if (target < mid) return binarySearch2(arr, start, midIndex - 1, target)
    return binarySearch2(arr, midIndex + 1, end, target)
}


// const result = binarySearch(arr, 3)
// console.log(result)

const result = binarySearch2(arr, start, end, 11)
console.log(result)