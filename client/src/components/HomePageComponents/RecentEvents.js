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
    <div className="w-full max-w-md p-4 xl:p-8 card mb-5 h-min">
    <div className="flex items-center justify-between mb-4">
        <h5 className="titleTextDiv">What's New!</h5>
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
                    <p className="bodyTextDiv font-semibold hover:text-[#0075FF] hover:underline">
                        {item.event}
                    </p>
                    <p className="bodyTextDiv">
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
