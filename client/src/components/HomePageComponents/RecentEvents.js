// Setting the environment to use client-side rendering
"use client";

// Importing React, useState, and Link from Next.js
import React from 'react'
import { useState } from 'react';
import Link from 'next/link';

// Functional component for rendering recent events
export default function RecentEvents() {
    // State variable to store recent events data
    const [recentEvents, setRecentEvents] = useState([
        { event: "Dev Hackathon", date: new Date(2023, 11, 3) }, 
        { event: "Enosium Hackathon", date: new Date(2023, 11, 3) },
        { event: "Inter IIT'23", date: new Date(2023, 11, 3) },
      ]);
    
      // JSX structure for rendering the recent events component
  return (
    <div className="w-full max-w-md p-4 xl:p-8 card mb-5 h-min">
    <div className="flex items-center justify-between mb-4">
        {/* Heading for recent events */}
        <h5 className="titleTextDiv">What's New!</h5>
        {/* Link to view all recent events */}
        <Link href="#" className="text-sm font-medium text-[#0075FF] hover:underline">
            View all
        </Link>
   </div>
   <div className="flow-root">
        {/* List of recent events */}
        <ul role="list" className="divide-y divide-gray-200">
        {/* Mapping over recentEvents array to render individual event items */}
        {recentEvents.map((item) => (
        <li className="py-2 sm:py-4">
            {/* Individual event item structure */}
            <div className="flex items-center">
                <div className="flex-1 min-w-0 ms-4">
                    {/* Event name */}
                    <p className="bodyTextDiv font-semibold hover:text-[#0075FF] hover:underline">
                        {item.event}
                    </p>
                    {/* Event name */}
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
