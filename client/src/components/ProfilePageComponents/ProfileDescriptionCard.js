"use client";
import React from 'react'
import { useState } from 'react'

export default function ProfileDescriptionCard() {
  const [role, setRole] = useState("Web Developer")
  const [projectDescription, setProjectDescription] = useState("Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti beatae expedita eaque aspernatur natus quae omnis eum temporibus quod iste, nulla molestiae provident deserunt, cum numquam inventore asperiores nam exercitationem!")
  const [experience, setExperience] = useState("3 Years, 6 Months")
  return (
    <div className='m-5'>
      <div className="shadow-lg w-auto border border-gray-200 rounded-md p-5 text-gray-500">
        <div className="w-full text-center text-lg lg:text-2xl font-bold">About</div>
        <div className="shadow-lg border border-lg rounded-md p-4 my-4">
          <div className="text-lg lg:text-xl font-semibold">Role:</div>
          <div className="text-md lg:text-lg">{role}</div>
        </div>
        <div className="shadow-lg border border-lg rounded-md p-4 my-4">
          <div className="text-lg lg:text-xl font-semibold">Experience:</div>
          <div className="text-md lg:text-lg">{experience}</div>
        </div>
        <div className="shadow-lg border border-lg rounded-md p-4 my-4">
          <div className="text-lg lg:text-xl font-semibold">Profile Description:</div>
          <div className="text-md lg:text-lg">{projectDescription}</div>
        </div>
      </div>
    </div>
  )
}
