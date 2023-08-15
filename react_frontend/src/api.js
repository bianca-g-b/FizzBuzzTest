// store url base path in a variable
const baseUrl = "http://127.0.0.1:5000"

// write async function that fetches list of fizzBuzz nums from backend and returns it
// also include error handling
export async function getFizzBuzz() {
    try {
        const response = await fetch(`${baseUrl}/api/numbers`)
        const data = await response.json();
        return data
    } catch (error) {
        console.log("Error: ", error);
        return null
    }
}