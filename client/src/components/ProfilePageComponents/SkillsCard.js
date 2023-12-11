// Setting the environment to use client-side rendering
"use client";

// Importing React, 'useEffect', and 'useState' hook
import React, { useEffect } from "react";
import { useState } from "react";

// Functional component for rendering a skills card
export default function SkillsCard({ ele }) {
  // JSX structure for the skills card
  return (
    <div className="w-auto card m-5 h-min">
      {/* Present Skills section */}
      <div className="my-3 rounded-md p-3 border border-gray-200">
        <h2 className="titleCard">Present Skills</h2>
        {/* Mapping through present skills and displaying them */}
        {ele?.data?.skills?.map((item, index) => {
          return (
            <div
              key={index}
              className="p-4 my-3 bodyCard border border-gray-200 shadow-md"
            >
              {item}
            </div>
          );
        })}
      </div>
      {/* Skills Recommended by Trumio section */}
      <div className="my-3 rounded-md p-3 border border-gray-200">
        <h2 className="titleCard">Skills Recommended by Trumio</h2>
        {/* Mapping through recommended skills and displaying them */}
        {ele?.data?.learning_resources?.map((ele, index) => {
          return (
            <div key={index}>
              {/* Redirecting to the URL when a recommended skill is clicked */}
              <div
                onClick={() => {
                  window.location.href = ele.url;
                }}
                className="p-4 my-3 bodyCard border border-gray-200 shadow-md"
              >
                {ele.title}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
