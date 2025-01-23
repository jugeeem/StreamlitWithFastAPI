"use client";

export default function Home() {
  async function sendMessage() {
    // "use server";
    const formData = new FormData();
    formData.append("username", "sample2");
    formData.append("email", "test@test.test");
    formData.append("password", "sample");
    const json = JSON.stringify(Object.fromEntries(formData));

    await fetch("http://localhost/api/v1/auth/signup/", {
      method: "POST",
      body: json,
      headers: {
        'Content-Type': 'application/json',
      },
    }).then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("Something went wrong");
      }
    }).catch((error) => {
      console.error("Error:", error);
    });
  }

  return (
    <div>
      <form action="http://localhost/api/v1/auth/signup" method="POST">
        <input type="text" name="username" /> <br />
        <input type="text" name="email" /><br />
        <input type="password" name="password" /><br />
        <button type="submit">送信</button>
      </form>
      <button onClick={sendMessage}>fetch</button>
    </div>
  );
}
