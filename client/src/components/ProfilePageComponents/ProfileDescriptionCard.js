// Setting the environment to use client-side rendering
"use client";

// Importing React and the 'useState' hook
import React, { useState } from "react";

// Functional component for rendering a profile description card
export default function ProfileDescriptionCard({ ele }) {
  // State variables for profile description information
  const [role, setRole] = useState("Web Developer");
  const [projectDescription, setProjectDescription] = useState(
    "Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti beatae expedita eaque aspernatur natus quae omnis eum temporibus quod iste, nulla molestiae provident deserunt, cum numquam inventore asperiores nam exercitationem!"
  );
  const [experience, setExperience] = useState("3 Years, 6 Months");

  // JSX structure for the profile description card
  return (
    <div className="m-5">
      <div className="w-auto border border-gray-200 rounded-md card">
        {/* Card heading */}
        <div className="w-full text-center headingCard">About</div>
        {/* Role section */}
        <div className="card !p-4 shadow-md my-4">
          <div className="titleTextDiv">Role:</div>
          <div className="bodyTextDiv">{ele?.data?.role}</div>
        </div>
        {/* Experience section */}
        <div className="card !p-4 shadow-md my-4">
          <div className="titleTextDiv">Experience:</div>
          <div className="bodyTextDiv">{experience}</div>
        </div>
        {/* Profile Description section */}
        <div className="card !p-4 shadow-md my-4">
          <div className="titleTextDiv">Profile Description:</div>
          <div className="bodyTextDiv">{projectDescription}</div>
        </div>
      </div>
    </div>
  );
}
