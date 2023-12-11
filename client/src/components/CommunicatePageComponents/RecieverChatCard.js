// Setting the environment to use client-side rendering
"use client";

// Importing React and useState from React
import React from "react";
import { useState } from "react";

// Functional component for rendering a chat card for the receiver
export default function RecieverChatCard({ ele }) {
  // JSX structure for rendering the receiver's chat card
  return (
    <div className="flex items-center p-5">
      {/* Displaying the receiver's profile image */}
      <img
        src="https://www.gravatar.com/avatar/2acfb745ecf9d4dccb3364752d17f65f?s=260&d=mp"
        alt=""
        className="w-16 h-16 rounded-full"
      />

      {/* Displaying the receiver's message with styling */}
      <div className="text-md xl:text-lg text-gray-600 p-5 rounded-lg shadow-lg mx-5">
        {ele.message}
      </div>
    </div>
  );
}
