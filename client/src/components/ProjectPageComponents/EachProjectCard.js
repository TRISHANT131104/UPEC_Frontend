'use client'
import React from 'react'
import parse from 'html-react-parser';
export default function
    ({ ele }) {
    return (
        <div>
            <div className="flex justify-center w-full">
                <div className="max-w-full">
                    <div className="bg-white shadow-[2px_2px_2px_2px] rounded-md py-3">
                        <div className="p-2">
                            <div className="text-md my-3 ">
                                <div><div className='grid grid-cols-[auto_auto]'>
                                    <div className="px-2 py-2 text-gray-500 font-semibold">Skills Required</div>
                                    <div className='flex flex-wrap'>
                                        {ele?.related_techstacks.map((item, index) => {
                                            return (
                                                <div key={index} className="px-2 py-2">
                                                    {item}
                                                </div>
                                            )
                                        })}
                                    </div>
                                </div>
                                    <div className='grid grid-cols-[auto_auto] '>
                                        <div className="px-2 py-2 text-gray-500 font-semibold">Bid Price</div>
                                        <div className="px-2 py-2 !text-start !justify-start">{ele?.bid_price}</div>
                                    </div>
                                    <div className='grid grid-cols-[auto_auto] '>
                                        <div className="px-2 py-2 text-gray-500 font-semibold">Start Date</div>
                                        <div className="px-2 py-2 !w-full !text-start !justify-start">{ele?.start_date}</div>
                                    </div>
                                    <div className='grid grid-cols-[auto_auto] '>
                                        <div className="px-2 py-2 text-gray-500 font-semibold">End Date</div>
                                        <div className="px-2 py-2 !w-full !text-start !justify-start">{ele?.end_date}</div>
                                    </div>
                                    <div className='grid grid-cols-[auto_auto] '>
                                        <div className="px-2 py-2 text-gray-500 font-semibold">Project Timeline</div>
                                        <div className="px-2 py-2 !w-full !text-start !justify-start">{ele?.project_timeline}</div>
                                    </div>
                                    <div className='grid grid-cols-[auto_auto] '>
                                        <div className="px-2 py-2 text-gray-500 font-semibold">project status</div>
                                        <div className="px-2 py-2 !w-full !text-start !justify-start">{ele?.status}</div>
                                    </div>
                                    <div className='grid grid-cols-[auto_auto] '>
                                        <div className="px-2 py-2 text-gray-500 font-semibold">Project Owner</div>
                                        <div className="px-2 py-2 !w-full !text-start !justify-start">{ele?.created_by?.user?.username}</div>
                                    </div>
                                </div></div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    )
}
