import Form from 'next/form';
import { redirect } from 'next/navigation';
import Login from '@/features/auth/login';
// import { actionLogin } from '@/features/auth/login/actions';

export default async function Page() {

  async function actionLogin(formData: FormData) {
    "use server";
    const payload = new URLSearchParams();
    payload.append("username", formData.get("username") as string);
    payload.append("password", formData.get("password") as string);
    try {
      const response = await fetch("http://backend:8000/api/v1/auth/token", {
        method: "POST",
        body: payload,
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });
      if (response.ok) {
        const json = await response.json();
        console.log(json);
        // localStorage.setItem("token", json.access_token);
        redirect("/");
      } else {
        throw new Error("Something went wrong");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }
  return (
    <div className='flex justify-center items-center m-8'>
      <Form action={actionLogin}>
        <Login />
      </Form>
    </div>
  )
}
