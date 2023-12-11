"use client";
import React from 'react'
import { useState } from 'react';
import Link from 'next/link';

export default function recentChatCard(){
    const [recentChats, setRecentChats] = useState([
        { name: "John Doe", email: "johndoe@gmail.com", image_url:"https://www.gravatar.com/avatar/2acfb745ecf9d4dccb3364752d17f65f?s=260&d=mp" }, 
        { name: "Jack", email: "jack1234@gmail.com", image_url:"https://www.gravatar.com/avatar/2acfb745ecf9d4dccb3364752d17f65f?s=260&d=mp" },
        { name: "Tim", email: "tim5678@gmail.com", image_url:"https://www.gravatar.com/avatar/2acfb745ecf9d4dccb3364752d17f65f?s=260&d=mp"},
      ]);
  return (
<div className="w-full max-w-md p-4 xl:p-8 card h-min">
    <div className="flex items-center justify-between mb-4">
        <h5 className="titleTextDiv">Recent Chats</h5>
        <Link href="#" className="text-sm font-medium text-[#0075FF] hover:underline">
            View all
        </Link>
   </div>
   <div className="flow-root">
        <ul role="list" className="divide-y divide-gray-200">
        {recentChats.map((item) => (
        <li className="py-3 sm:py-4">
            <div className="flex items-center">
                <div className="flex-shrink-0">
                    <img className="w-8 h-8 rounded-full" src={item.image_url} alt="Neil image"/>
                </div>
                <div className="flex-1 min-w-0 ms-4">
                    <p className="bodyTextDiv font-semibold">
                        {item.name}
                    </p>
                    <p className="bodyTextDiv">
                        {item.email}
                    </p>
                </div>
            </div>
        </li>
      ))}
        </ul>
   </div>
</div>
  )
}
