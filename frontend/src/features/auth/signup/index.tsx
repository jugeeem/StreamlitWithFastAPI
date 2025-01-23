"use client";

import { Input, Button } from "@heroui/react";


export default function Signup() {
  return (
    <>
      <Input name="username" label="username" type="text" className="m-4" />
      <Input name="email" label="email" type="email" className="m-4" />
      <Input name="password" label="password" type="password" className="m-4" />
      <Button type="submit" className="m-4">Signup</Button>
    </>
  )
}