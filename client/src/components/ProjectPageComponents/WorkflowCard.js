// Importing React library
import React from 'react';

// Functional component for rendering Workflow Card
export default function WorkflowCard(props) {

    return (
        <div className="flex-col text-[#414141] mt-4 w-full">
            {/* Checking if workflowData is available */}
            {props.workflowData ? (
                // Mapping through each user in workflowData
                Object.keys(props.workflowData).map((key, index) => (
                    <div key={index} className="mb-4 px-4">
                        {/* Displaying User and their roles */}
                        <h1 className="text-lg font-bold">User: {key}</h1>
                        <div className="mt-2 px-4">
                            {/* Displaying User's roles */}
                            <h2 className="text-md font-semibold">Roles:</h2>
                            <ul className="list-disc pl-5">
                                <li className="text-sm">{props.workflowData[key].roles}</li>
                            </ul>
                        </div>
                        <div className="mt-2 px-4">
                            {/* Displaying User's tasks */}
                            <h2 className="text-md font-semibold">Tasks:</h2>
                            <ul className="list-disc pl-5">
                                <li className="text-sm">{props.workflowData[key].tasks}</li>
                            </ul>
                        </div>
                    </div>
                ))
            ) : (
                // Displaying a message when no Workflow Data is available
                <p className="text-md text-gray-500">No Workflow Data</p>
            )}
        </div>
    );
}