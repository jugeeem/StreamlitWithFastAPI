"use server";

import { redirect } from 'next/navigation'

export async function actionLogin(formData: FormData) {
  const json = JSON.stringify(Object.fromEntries(formData));

  await fetch("http://localhost/api/v1/auth/token/", {
    method: "POST",
    body: json,
    headers: {
      'Content-Type': 'application/json',
    },
  }).then((response) => {
    if (response.ok) {
      // return response.json();
      redirect("/auth/login");
    } else {
      throw new Error("Something went wrong");
    }
  }).catch((error) => {
    console.error("Error:", error);
  });
}

