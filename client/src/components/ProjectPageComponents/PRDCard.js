import React from 'react'
import parse from 'html-react-parser';
export default function PRDCard({ele,EachProject}) {
    
    return (
        <div className=''>
             <h1 className='text-center headingTextDiv uppercase'>{ele.replace("_"," ")}</h1>
                    <div id="learning_resources">
                        {EachProject?.data?.prd ? parse(EachProject.data.prd[ele]) : null}
                    </div>
        </div>
    )
}