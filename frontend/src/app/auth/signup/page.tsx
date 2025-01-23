import Form from 'next/form'
import { redirect } from 'next/navigation'

import Signup from '@/features/auth/signup'
// import { createUser } from '@/features/auth/signup/actions'

export default async function Page() {
  async function createUser(formData: FormData) {
    "use server";
    const json = JSON.stringify(Object.fromEntries(formData));
  
    await fetch("http://backend:8000/api/v1/auth/signup", {
      method: "POST",
      body: json,
      headers: {
        'Content-Type': 'application/json',
      },
    }).then((response) => {
      console.log(response);
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
  
  return (
    <div className='flex justify-center items-center m-8'>
      <Form action={createUser}>
        <Signup />
      </Form>
    </div>
  )
}
