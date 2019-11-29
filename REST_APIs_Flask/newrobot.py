*** Settings ***
Documentation
...    Responsible tester:  pawel.zuczkowski@nokia.com

#Resource         ../resources/setup_and_teardown.robot
#Resource         ./variables.robot
#Resource         ../resources/scenarios/scenarios.robot
Resource      resources/WMP/GVe/Wroclaw/bts_scfc.robot

#Library          ../resources/python_libs/TestCaseRequirement.py
Library          ute_reporting_portal
Library          ute_admin
Library          ute_admin_infomodel
Library          BuiltIn
Library          Collections
Library          String
Library          Keywords.py

#Suite Setup      Setup Test Set IPHY   ${SCFC_REFERENCE_FILE_PATH}
##Suite Teardown   Teardown Test Set IPHY

*** Variables ***
${SCFC_REFERENCE_FILE_PATH}=            ${CURDIR}/SCFC_FL19A.xml
${CONFIGURATION_NAME}=                  60_2a2
${DIST_NAME}=                       /MRBTS-1/RAT-1/RUNTIME_VIEW-1/MRBTS_R-1/LNBTS_R-1/LNCEL_R-1
${path}=                            /MRBTS-1/RAT-1/MCTRL-1/BBTOP_M-1/MRBTS_M-1/LNBTS_M-1/CELL_M-1/LNCEL_M-1
${scfc_file_path}                 /home/ute/robotlte/testsuite/WMP/GVe/Wroclaw/AiFSiteS/IPHY/60_2a2_FRIG_FRHF_RB/SCFC_FL19A.xml


*** Test Cases ***
Create LcrdID and LNcelId List
    ${out_lcr_id_list}     ${out_lncel_id_list}=    Create LcrdID and LNcelId List    ${scfc_file_path}
    ${out_lcr_id_list}=    set global variable    ${out_lcr_id_list}
    ${out_lncel_id_list}=   set global variable    ${out_lncel_id_list}
#    ${x}=    Evaluate    ${out_lcr_id_list[2]}==${out_lncel_id_list[3]}
#    Should Be Equal    ${out_lcr_id_list[2]}     ${out_lncel_id_list[3]}

Setup Admin and Infomodel
    Setup admin    bts_host=192.168.255.1    bts_port=443    use_ssl=True
    ute_admin_infomodel.Setup infomodel    address=192.168.255.1    port=443    use_ssl=True
    ute_admin_infomodel.connect_infomodel

Check If Identical Cells Have The Same Cablink
    ${out_cell_information}=    Get Cell Information    ${out_lncel_id_list}
    ${out_cablink_information}=    Get Cablink Information for All Cells     ${out_lcr_id_list}
    ${out_cell_information_values}=    Get Dictionary Values    ${out_cell_information}
    ${out_cell_information_keys}=    Get Dictionary Keys    ${out_cell_information}
    ${mapping}=     Create Mapping    ${out_cell_information_keys}
    ${out_identical_cells}=   Find Indentical Cells      ${out_cell_information_values}
    ${out_mapped_identical_cells}=    Create Identical Cells List    ${out_cell_information_keys}    ${out_cell_information_values}
    :FOR    ${CELL}    IN    @{out_mapped_identical_cells}
    \    ${x}=    Get From Dictionary    ${out_cablink_information}   ${CELL[0]}
    \    ${y}=    Get From Dictionary    ${out_cablink_information}   ${CELL[1]}
    \    should be equal    ${x}   ${y}


*** Keywords ***
Create LcrdID and LNcelId List
    [Arguments]      ${scfc_file_path}
    ${out_lcr_id_list}=    SCFC Create LcrId List    ${scfc_file_path}
    ${out_lncel_id_list}=    SCFC Create LncelId List    ${scfc_file_path}
    [Return]     ${out_lcr_id_list}     ${out_lncel_id_list}

Get Cablink Information for All Cells
    [Documentation]  Keyword is used to create list of cablink information (- which cablink is used to route cell) for all cells
    ...     Author: pawel.zuczkowski@nokia.com
    [Arguments]    ${out_lcr_id_list}
    ${out_cablink_information}=    Create Dictionary
    :FOR    ${LCR_ID}    IN     @{out_lcr_id_list}
    \    ${out_results}     @{out_lncel_M}=     ute_admin_infomodel.Query Infomodel    query=get list //CELL_M-${LCR_ID}/CHANNEL_GROUP_M-1/CHANNEL_M-*/DEVICES_LIST-1
    \    ${out_cell_cablink_information}=    Get Cablink Info for Cell    ${out_lncel_M}
    \    Set To Dictionary     ${out_cablink_information}    ${LCR_ID}    ${out_cell_cablink_information}
    [Return]     ${out_cablink_information}

Get Cablink Info for Cell
    [Documentation]  Keyword is used to check which cablink is used to route cell
    ...     Author: pawel.zuczkowski@nokia.com
    [Arguments]    ${channel_m_device_list}
    @{out_cell_cablink_information}=    Create List
    ${number}=    Get Length    ${channel_m_device_list}
    :FOR    ${index}     IN RANGE     -1    ${number}
    \    ${x} =    Get From List    ${channel_m_device_list}    ${index}
#    \    Should Match Regexp
    \    ${value}=       Get From Dictionary     ${x}     deviceDNs
    \    ${cablink_index}=      Check which value in dictionary match regexp    ${value}
    \
#    \    ${length}=    Get Length    ${value}
    \    ${dic} =      Get From List    ${value}    ${cablink_index}
    \    ${cablink_list}=    Get From Dictionary    ${dic}    deviceDN
    \    @{words}=     Split String    ${cablink_list}    /
    \    ${cablink}=    Set Variable     ${words[7]}
    \    Append To List     ${out_cell_cablink_information}    ${cablink}
    [Return]    ${out_cell_cablink_information}

Get Cell Information
    [Documentation]  Keyword is used to create list of cells with information (earfcnDl, dlChBw)
    ...     Author: pawel.zuczkowski@nokia.com
    [Arguments]     ${lncel_id_list}
    ${out_cell_information}=    Create Dictionary
    :FOR    ${LNCEL_ID}    IN    @{lncel_id_list}
    \    ${out_lncel_M}=      ute_admin_infomodel.Query Infomodel    query=get object //LNCEL_M-${LNCEL_ID}
    \    ${earfcnDl}=    Get From Dictionary    ${out_lncel_M}   earfcnDl
    \    ${dlChBw}=    Get From Dictionary    ${out_lncel_M}   dlChBw
    \    @{cell_info}=    Create List      ${earfcnDl}    ${dlChBw}
    \    Set To Dictionary     ${out_cell_information}    ${LNCEL_ID}    ${cell_info}
    [Return]    ${out_cell_information}

Check which value in dictionary match regexp
    [Arguments]     ${dictionary}
    ${lenght}=    get length     ${dictionary}
    @{cablink_list}=    Create List
    :FOR    ${index}    IN RANGE   0    ${lenght}
    \    ${Cablink}=    Get From Dictionary    ${dictionary}   ${index}
    \    ${Cablink}=    Get From Dictionary    ${Cablink}   deviceDN
    \    ${status}    ${value}=    Run Keyword and Ignore Error     Should Match Regexp    ${Cablink}   CABLINK
    \    Run Keyword if    '${status}' == 'PASS'    append to list     ${cablink_list}   ${index}
    ${cablink_index}=    Get From List    ${cablink_list}    0
    [Return]     ${cablink_index}
