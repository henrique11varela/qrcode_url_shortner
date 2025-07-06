async function request(url, method = "GET", body = null) {
    const res = await fetch(`${url}`, {
        method: `${method}`,
        headers: {
            "Content-Type": "application/json",
        },
        ...((method != "GET" && body) && {
            body: JSON.stringify(body)
        })
    })
    const data = await res.json()
    console.log(data);
    
    return data
}