// Setting the environment to use client-side rendering
"use client";

// Importing React, useState, and Link from Next.js
import React from 'react'
import { useState } from 'react';
import Link from 'next/link';

// Functional component for rendering a recent chat card
export default function recentChatCard(){
    // State variable to store recent chat data
    const [recentChats, setRecentChats] = useState([
        { name: "John Doe", email: "johndoe@gmail.com", image_url:"https://www.gravatar.com/avatar/2acfb745ecf9d4dccb3364752d17f65f?s=260&d=mp" }, 
        { name: "Jack", email: "jack1234@gmail.com", image_url:"https://www.gravatar.com/avatar/2acfb745ecf9d4dccb3364752d17f65f?s=260&d=mp" },
        { name: "Tim", email: "tim5678@gmail.com", image_url:"https://www.gravatar.com/avatar/2acfb745ecf9d4dccb3364752d17f65f?s=260&d=mp"},
      ]);

    // JSX structure for rendering the recent chat card
  return (
<div className="w-full max-w-md p-4 xl:p-8 card h-min">
    <div className="flex items-center justify-between mb-4">
        {/* Heading for recent chats */}
        <h5 className="titleTextDiv">Recent Chats</h5>
        {/* Link to view all recent chats */}
        <Link href="#" className="text-sm font-medium text-[#0075FF] hover:underline">
            View all
        </Link>
   </div>
   <div className="flow-root">
        {/* List of recent chats */}
        <ul role="list" className="divide-y divide-gray-200">
        {/* Mapping over recentChats array to render individual chat items */}
        {recentChats.map((item) => (
        <li className="py-3 sm:py-4">
            {/* Individual chat item structure */}
            <div className="flex items-center">
                <div className="flex-shrink-0">
                    {/* User profile image */}
                    <img className="w-8 h-8 rounded-full" src={item.image_url} alt="Neil image"/>
                </div>
                <div className="flex-1 min-w-0 ms-4">
                    {/* User name */}
                    <p className="bodyTextDiv font-semibold">
                        {item.name}
                    </p>
                    {/* User email */}
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
