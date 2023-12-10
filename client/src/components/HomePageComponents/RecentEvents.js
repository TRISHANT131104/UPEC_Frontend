"use client";
import React from 'react'
import { useState } from 'react';
import Link from 'next/link';

export default function RecentEvents() {

    const [recentEvents, setRecentEvents] = useState([
        { event: "Dev Hackathon", date: new Date(2023, 11, 3) }, 
        { event: "Enosium Hackathon", date: new Date(2023, 11, 3) },
        { event: "Inter IIT'23", date: new Date(2023, 11, 3) },
      ]);
      
  return (
    <div className="w-full max-w-md p-4 xl:p-8 bg-white border border-gray-200 rounded-lg shadow-xl text-[#5E5873] basis-1/2 mb-5">
    <div className="flex items-center justify-between mb-4">
        <h5 className="text-lg xl:text-xl font-bold leading-none text-[#5E5873]">What's New!</h5>
        <Link href="#" className="text-sm font-medium text-[#0075FF] hover:underline">
            View all
        </Link>
   </div>
   <div className="flow-root">
        <ul role="list" className="divide-y divide-gray-200">
        {recentEvents.map((item) => (
        <li className="py-2 sm:py-4">
            <div className="flex items-center">
                <div className="flex-1 min-w-0 ms-4">
                    <p className="text-sm font-medium text-[#5E5873] truncate hover:text-[#0075FF] hover:underline">
                        {item.event}
                    </p>
                    <p className="text-sm text-[#5E5873] truncate">
                        {item.date.toLocaleDateString()}
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
