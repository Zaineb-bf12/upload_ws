import boto3
from kor.extraction import create_extraction_chain
from kor.nodes import Object, Text
from langchain_community.llms import Bedrock

# Define the schema for extraction.
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Union
# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name= "us-east-1")

# Set the model ID, e.g., Llama 3 8b Instruct.
# model_id = "meta.llama3-70b-instruct-v1:0"
# model_id = "mistral.mistral-small-2402-v1:0"
# model_id = "amazon.titan-text-lite-v1"
model_id = "mistral.mistral-large-2402-v1:0"
# model_id = "mistral.mixtral-8x7b-instruct-v0:1"

# Initialize the Bedrock instance.
llm = Bedrock(
    model_id=model_id
)
schema = Object(
    id="Potential Candidate",
    description=(
        "Extracting information related to the candidate, their professional experience, and education from the CV."
    ),
    attributes=[
        Object(
            id="Experiences",
            description=(
                "Professional experience and internships represent the accumulation of knowledge and skills acquired through practice. This section encompasses the various roles a person has held in the past and present, whether through paid employment, internships, volunteer work, or other relevant experiences. "
                "It encompasses the various roles held by an individual in the past and present, whether through paid jobs, internships, volunteer work, or other relevant experiences. "
                "This section of the CV provides a detailed overview of an individual's career path, highlighting responsibilities assumed, skills acquired, and achievements. "
                "It should include the following information: "
                "- Company Name: Full name of the company. "
                "- Job Title: Title or role held. "
                "- Employment Dates: Start and end period (month/year - month/year). "
                "- Achievements: This section summarizes the achievements and responsibilities, encompassing all the tasks accomplished during this professional experience. "
            ),
            attributes=[
                Text(
                    id="companyName",
                    description="Full name of the company",
                    type="string"
                ),
                Text(
                    id="country",
                    description="Country where the company is located.",
                    type="string"
                ),
                Text(
                    id="role",
                    description="Title or role held in the company",
                    type="string"
                ),
                Text(
                    id="startDate",
                    description="Start date of the experience",
                    type="date"
                ),
                Text(
                    id="endDate",
                    description="End date of the experience",
                    type="date"
                ),
                Text(
                    id="achievements",
                    description="This section summarizes the achievements and responsibilities, including an overview of the tasks accomplished and the role held within this company.",
                    type="string"
                ),
                Object(
                    id="missions",
                    description=(
                        "All missions, projects, and phases completed within the company. This includes a detailed description of the tasks performed, as well as the skills implemented."
                    ),
                    attributes=[
                        Text(
                            id="projectName",
                            type="string",
                            description="Name of the completed project."
                        ),
                        Text(
                            id="description",
                            type="string",
                            description="Detailed description of the tasks and responsibilities of the mission."
                        ),
                        Text(
                            id="skills",
                            type="array",
                            description="Skills related to this mission.",
                            items={
                                "type": "string",
                                "description": "Specific skill used or developed during the mission."
                            }
                        ),
                        Text(
                            id="projectDate",
                            type="date",
                            description="Date of project completion."
                        )
                    ],
                    many=True,
                    # Ensure projects are displayed in reverse chronological order
                    sort_by="projectDate",
                    sort_order="desc"
                )
            ],
            many=True
        )
    ],
    many=False
)

schema1 = Object(
    id="Potential Candidate",
    description=(
        "Extracting information related to the candidate, their professional experience, and education from the CV."
    ),
    attributes=[
        Object(
            id="Education",
            description=(
                "The education section allows evaluating the academic qualifications of a candidate. "
                "It should be written concisely and informatively, highlighting the skills and knowledge acquired by the candidate during their studies. "
                "It should include the following information: "
                "- Institutions attended: Indicate the full name of the institution, the level of study, and the duration of studies. "
                "- Degrees obtained: Indicate the name of the degree, the date of graduation, and honors, if applicable. "
                "- Other relevant academic achievements: Indicate any academic achievement that is relevant to the position applied for."
            ),
            attributes=[
                Text(
                    id="institutionName",
                    description="Full name of the institution",
                    type="string"
                ),
                Text(
                    id="degree",
                    description="Name of the degree obtained",
                    type="string"
                ),
                Text(
                    id="studyLevel",
                    description="Level of study attained",
                    type="string"
                ),
                Text(
                    id="studyDuration",
                    description="Duration of studies (from - to)",
                    type="string"
                ),
                Text(
                    id="graduationDate",
                    description="Date of degree completion",
                    type="date"
                )
            ],
            many=True
        ),
        Text(
            id="Name",
            description="The name should be indicated at the top of the page, in uppercase, followed by the first name.",
            type="string"
        ),
        Text(
            id="Email",
            description="The email should be unique and correspond as much as possible to the candidate's name. "
                        "It is used for official communications and must be professional. "
                        "Ensure the email address is correct and active.",
            type="string"
        ),
        Text(
            id="LinkedIn",
            description="Link to the LinkedIn profile.",
            type="string"
        ),
        Text(
            id="GitHub",
            description="Link to the GitHub profile.",
            type="string"
        ),
        Text(
            id="Twitter",
            description="Link to the Twitter profile.",
            type="string"
        ),
        Text(
            id="Address",
            description="Residential or professional address.",
            type="string"
        ),
        Text(
            id="Date of Birth",
            description="Date of birth in the format YYYY-MM-DD.",
            type="string"
        ),

        Text(
            id="Phone Number",
            description="A phone number is a series of digits uniquely identifying a terminal in a telecommunications network.",
            type="string"
        ),
        Text(
            id="profile_title",
            description="The profile title should be displayed at the top of the page, in uppercase. It can be composed of the most recent professional experience according to the chronology.",
            type="string"
        ),
        Object(
            id="Languages",
            description=(
                "Languages spoken and level of proficiency."
            ),
            attributes=[
                Text(
                    id="language",
                    description="Full name of the language",
                    type="string"
                ),
                Text(
                    id="proficiency",
                    description="Level of proficiency",
                    type="string"
                )
            ],
            many=True
        ),
        Text(
            id="years_of_experience",
            description="Number of years of experience, which is the sum of all experiences.",
            type="string"
        ),
        Text(
            id="Certifications",
            description="This section should contain the name of the certification, the issuing organization, and the date of obtaining.",
            type="string"
        ),
        Object(
            id="Certifications",
            description=(
                "This section should contain the name of the certification, the issuing organization, and the date of obtaining."
            ),
            attributes=[
                Text(
                    id="name",
                    description="Full name of the certification",
                    type="string"
                ),
                Text(
                    id="organization",
                    description="Issuing organization",
                    type="string"
                ),
                Text(
                    id="date",
                    description="Date of obtaining",
                    type="string"
                )
            ],
            many=True
        ),
        Object(
            id="Skills",
            description=(
                "Skills can be technical (hard skills), such as proficiency with software or a foreign language, or non-technical (soft skills), such as the ability to communicate, work in a team, or solve problems."
            ),
            attributes=[
                Text(
                    id="skill",
                    description="Full name of the skill",
                    type="string"
                ),
                Text(
                    id="level",
                    description="Level of proficiency",
                    type="string"
                )
            ],
            many=True
        )
    ],
    many=False
)

# Fonction pour exécuter la chaîne d'extraction avec le premier schéma
def txt_json(txt):
    chain = create_extraction_chain(llm, schema, encoder_or_encoder_class='json')
    res = chain.run(txt)['data']
    return res

# Fonction pour exécuter la chaîne d'extraction avec le deuxième schéma
def txt_json1(txt):
    chain1 = create_extraction_chain(llm, schema1, encoder_or_encoder_class='json')
    res1 = chain1.run(txt)['data']
    return res1

# Fonction principale pour traiter le texte du CV et combiner les deux JSON
def extract_and_combine(txt):
    res = txt_json(txt)
    res1 = txt_json1(txt)
    # result = merge(res, res1)
    # combined_res ={**json.loads(res), **json.loads(res1)}  # Combiner les deux dictionnaires JSON
    return res1,res
# conversation = Con versationChain(
#     llm=llm, verbose=True, memory=ConversationBufferMemory()
# )
# response = conversation.predict(input="bonjour")
# print(response)

