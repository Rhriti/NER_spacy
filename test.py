import spacy
from spacy.training.example import Example
from spacy.displacy import render


# Load your fine-tuned model
nlp_ner= spacy.load('./model-best')
test_data=[
    'If the floor mat moves out of position and interferes with the accelerator or brake pedal operation, it can increase the risk of a crash.	Subaru has notified owners, and dealers will inspect the floor mat retention bracket and replace it if necessary, free of charge.  The recall began November 14, 2017.  Owners may contact Subaru customer service at 1-800-782-2783.  Subaru number for this recall is WTR-77.	Owners may also contact the National Highway Traffic Safety Administration Vehicle Safety Hotline at 1-888-327-4236 (TTY 1-800-424-9153), or go to www.safercar.gov.'
,'THE RIVETS MUST BE REPLACED WITH THE CORRECT BOLTS.	SYSTEM: INTERIOR SYSTEMS: SEAT TRACKS AND ANCHORS; REAR SEAT; FMVSS 207.VEHICLE DESCRIPTION: LIGHT-DUTY TRUCKS; 1-TON CREW CAB PICKUP TRUCKS EQUIPPEDWITH AM7 FOLDING REAR BENCH SEAT.CONSEQUENCE OF DEFECTS: IN AN ACCIDENT, THE SEAT WOULD BECOME DETACHEDCAUSING INJURIES TO THE SEAT OCCUPANTS OR OTHER OCCUPANTS IN THE TRUCK.NOTE: IF YOUR VEHICLE IS PRESENTED TO AN AUTHORIZED DEALER ON AN AGREED UPONSERVICE DATE AND THE REMEDY IS NOT PROVIDED WITHIN A REASONABLE TIME AND FREEOF CHARGE OR THE REMEDY DOES NOT CORRECT THE DEFECT OR NONCOMPLIANCE, PLEASECONTACT THE CHEVROLET SERVICE CENTER AT 1-800-222-1020 OR GMC TRUCK SERVICECENTER AT 1-313-456-4547. ALSO, CONTACT THE NATIONAL HIGHWAY TRAFFIC SAFETYADMINISTRATION AUTO SAFETY HOTLINE AT 1-800-424-9393.'
,'THIS CONDITION CAN CONTINUE TO DETERIORATE AND WILL EVENTUALLY RESULT IN THE BALL JOINT STUD SEPARATING FROM THE HOUSING INCREASING THE RISK OF LOSS OF VEHICLE CONTROL.	MOOG WILL REPLACE THESE BALL JOINTS WITH BALL JOINTS FROM ANOTHER SUPPLIER.	OWNER NOTIFICATION BEGAN OCTOBER 12, 1998.OWNERS WHO DO NOT RECEIVE THE FREE REPLACEMENT BALL JOINTS WITHIN A REASONABLE TIME SHOULD CONTACT MOOG AT 1-314-385-3400.ALSO CONTACT THE NATIONAL HIGHWAY TRAFFIC SAFETY ADMINISTRATION AUTO SAFETY HOTLINE AT 1-888-DASH-2-DOT (1-888-327-4236).'
,'If the component detaches during deployment, the curtain air bag may not inflate properly during a crash, increasing the risk of injury.  Additionally, if the detached component were to enter the vehicle occupant compartment, there could be an increased risk of occupant injury.	Hyundai will notify owners, and dealers will replace the driver and passenger side curtain air bags, free of charge.  The recall is expected to begin February 9, 2018.  Owners may contact Hyundai customer service at 1-855-671-3059.  Hyundai number for this recall is 171.	Owners may also contact the National Highway Traffic Safety Administration Vehicle Safety Hotline at 1-888-327-4236 (TTY 1-800-424-9153), or go to www.safercar.gov.'
,'Improper air bag deployment can increase the risk of an injury.	Dealers will replace the trim parts, free of charge.  Owner notification letters were mailed May 27, 2022.  Owners may contact MBUSA customer service at 1-800-367-6372.  MBUSAs number for this recall is 2022050006. 	Owners may also contact the National Highway Traffic Safety Administration Vehicle Safety Hotline at 1-888-327-4236 (TTY 1-800-424-9153), or go to www.nhtsa.gov.'
,'FORD CAMPAIGN NO H7H.4X4 TRUCKS EQUIPPED W/6 CYLINDER ENGINES.POSSIBILITYTHAT AN INCORRECT REAR DRIVESHAFT WAS INSTALLED IN PRODUCTION.IFTHISCONDITION EXISTS THE DRIVESHAFT WILL VIBRATE AND DEFLECT AT HIGH SPEEDS.THIS VIBRATION AND DEFLECTION COULD CAUSE SHAFT TOBREAK.A BROKEN DRIVESHAFTMIGHT ADVERSELY AFFECT CONTROL OF VEHICLE.(CORRECT BY INSPECTING AND REPLACEWITH CORRECT DRIVESHAFT WHERE NECESSARY.'
,'If the fuel pump fails, the vehicle may stall without warning, increasing the risk of a crash.	Ford will notify owners, and dealers will replace the fuel pump, free of charge.  The recall began on February 27, 2015.  Owners may contact Ford customer service at 1-866-436-7332.  Fords number for this recall is 14S30. 	Owners may also contact the National Highway Traffic Safety Administration Vehicle Safety Hotline at 1-888-327-4236 (TTY 1-800-424-9153), or go to www.safercar.gov.'
,'IN THE EVENT OF A SEPARATION, THE FALLING GLASS COULD CREATE A ROAD HAZARD OR STRIKE A TRAILING VEHICLE, AND CAUSE A CRASH.	WEBASTO, THE MANUFACTURER OF THE SUNROOFS, WILL BE PERFORMING THE SAFETY RECALL CAMPAIGN.  OWNERS WHO HAVE BEEN IDENTIFIED AS HAVING AN AFFECTED SUNROOF INSTALLED IN THEIR VEHICLE WILL RECEIVE A SAFETY RECALL NOTICE FROM WEBASTO.   THE SAFETY RECALL BEGAN ON OCTOBER 8, 2010.  IN ORDER TO DETERMINE IF YOUR VEHICLE IS AFFECTED, PLEASE REVIEW THE LIST OF VEHICLES PROVIDED TO US BY M & M AUTOMOTIVE] BY CLICKING ON THE HYPERLINK <a href=http://www-odi.nhtsa.dot.gov/acms/docservlet/Artemis/Public/Recalls/2011/V/RCORRD-11V041-7676.pdf>AFFECTED VEHICLE LIST</a> OR YOU MAY VISIT WEBASTOS WEBSITE AT <a href=http://www.sunroofcheck.com> WWW.SUNROOFCHECK.COM</a>. YOU CAN ALSO CALL WEBASTO TOLL-FREE AT 1-888-749-8632.	OWNERS MAY ALSO CONTACT THE NATIONAL HIGHWAY TRAFFIC SAFETY ADMINISTRATIONS VEHICLE SAFETY HOTLINE AT 1-888-327-4236 (TTY 1-800-424-9153), OR GO TO <A HREF=HTTP://WWW.SAFERCAR.GOV>HTTP://WWW.SAFERCAR.GOV</A> .'
,'In the event of a fire, if the fire extinguisher does not function properly, it can increase the risk of injury.	"Volvo will notify owners, instructing them to contact Kidde for a replacement fire extinguisher, free of charge. The recall began on November 2, 2017.  Owners may contact Volvo customer service at 1-800-528-6586, or Kidde customer service toll-free at 1-855-262-3540, or online at www.kidde.com and click on ""Product Safety Recall"" for more information."	Owners may also contact the National Highway Traffic Safety Administration Vehicle Safety Hotline at 1-888-327-4236 (TTY 1-800-424-9153), or go to www.safercar.gov.'
,'THE DEALER WILL DO A TORQUE CHECK OF THE SELF-LOCKING NUTS AND, IF THE NUTS ARE FOUND TO BE LOOSE, THEY WILL BE TIGHTENED TO THE PROPER TORQUE SPECIFICATIONS, FREE OF CHARGE.	VEHICLE DESCRIPTION: PASSENGER VEHICLES.SYSTEM: STEERING; SELF LOCKING NUTS (STEERING COLUMN).CONSEQUENCES OF DEFECT: IF THE NUTS LOOSEN AND FALL OFF, THIS CAN LEAD TO LOSSOF VEHICLE CONTROL AND AN ACCIDENT.NOTE: PRIOR WARNING TO THE DRIVER SHOULD OCCUR IN THE FORM OF ABNORMAL STEERINGPLAY, CAUSED BY THE LOOSE NUTS.'
]


for ele in test_data:
    doc=nlp_ner(ele)
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))

    if entities:
        print("Found named entities:")
        for entity, label in entities:
            print(f"- {entity} ({label})")
    else:
        print("No named entities found in the text.")
    print('\n')

#For visual representation , won't render in terminal , run in google colab

# for ele in test_data:
#     doc=nlp_ner(ele)
#     spacy.displacy.render(doc,style="ent",jupyter=True)
#     print('\n')


