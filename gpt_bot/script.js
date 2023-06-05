let data = {
    "auth": { "reactivate": false, "username": "ali111111@gmail.com", "password": "12345678" }
  }
  async function getToken() {
    const response = await fetch("https://api.crystalknows.com/v3/user_token", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });
    const dts = await response.json();
    return dts.data.token;
  }
  
  let uuid = '4cbf6ee0-3fe4-4510-ac0f-6cca7102e8e5'
  const fetchData = async () => {
    const token = await getToken();
    const response = await fetch('https://main--crystal-ball-router.apollographos.net/graphql', {
      method: 'POST',
      headers: {
        'authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ query: `{ snapshot(uuid: "${uuid}") { personality { discTypeText } } }` })
    })
    const data = await response.json();
    console.log(data.data.snapshot.personality.discTypeText);
  }
  
  fetchData();