import React from 'react'
import parse from 'html-react-parser';
export default function PRDCard({ele,EachProject}) {
    
    return (
        <div>
             <h1 className='text-center font-bold text-black my-10 text-xl'>{ele}</h1>
                    <div id="learning_resources">
                        {EachProject?.data?.prd?EachProject.data.prd[ele]:null}
                    </div>
            
        </div>
    )
}
