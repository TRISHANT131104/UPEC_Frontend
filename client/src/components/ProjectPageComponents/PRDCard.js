// Importing required dependencies
import React from "react";
import parse from "html-react-parser";

// Functional component for rendering PRD card
export default function PRDCard({ ele, EachProject }) {
  return (
    <div className="">
      {/* Heading for the PRD card */}
      <h1 className="text-center font-bold text-black text-xl uppercase">
        {ele.replace("_", " ")}
      </h1>
      {/* Container for learning resources */}
      <div id="learning_resources">
        {/* Checking if PRD data is available and rendering it */}
        {EachProject?.data?.prd ? parse(EachProject.data.prd[ele]) : null}
      </div>
    </div>
  );
}
